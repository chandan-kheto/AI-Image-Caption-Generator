# ==============================================================
# 📁 backend/main.py
# FastAPI backend for AI Image Caption + Voice Generator (Free)
# ==============================================================

# Load .env from project root
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

# FastAPI imports
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

# Import our custom modules
from backend.caption_generator import caption_image_online   # Image → Caption
from backend.tts_voice import generate_voice                      # Caption → Voice (MP3)

# System tools
import os
import uuid


# --------------------------------------------------------------
# 🚀 Initialize FastAPI app
# --------------------------------------------------------------
app = FastAPI(title="AI Image Caption + Voice Generator (Free)")


# --------------------------------------------------------------
# 🌐 Enable CORS (Frontend → Backend communication)
# --------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Allow all frontend origins
    allow_credentials=True,
    allow_methods=["*"],          # Allow GET, POST, etc.
    allow_headers=["*"],
)

# Ensure temp folder exists
os.makedirs("backend/temp", exist_ok=True)


# --------------------------------------------------------------
# 🎨 Endpoint: POST /caption/online
# Input: Image file
# Output: Caption + MP3 voice path
# --------------------------------------------------------------
@app.post("/caption/online")
async def caption_online(file: UploadFile = File(...)):
    """
    Step 1: Receive uploaded image
    Step 2: Send image → OpenRouter → caption
    Step 3: Convert caption → MP3 using gTTS
    Step 4: Return caption + voice file path
    """

    # ----------------------------------------------------------
    # 1️⃣ Read uploaded image bytes
    # ----------------------------------------------------------
    image_bytes = await file.read()

    # Extract file extension (.jpg/.png)
    ext = os.path.splitext(file.filename)[1] or ".jpg"

    # Temporary unique file path
    temp_path = f"backend/temp/{uuid.uuid4()}{ext}"

    # Save image to temp folder
    with open(temp_path, "wb") as f:
        f.write(image_bytes)

    # ----------------------------------------------------------
    # 2️⃣ Generate caption using OpenRouter
    # ----------------------------------------------------------
    caption = caption_image_online(temp_path)

    # Remove the temporary image file to save space
    os.remove(temp_path)

    # ----------------------------------------------------------
    # 3️⃣ Convert caption → Speech (MP3)
    # ----------------------------------------------------------
    voice_path = generate_voice(caption)

    # ----------------------------------------------------------
    # 4️⃣ Return output JSON
    # ----------------------------------------------------------
    return {
        "caption": caption,
        "voice_path": voice_path
    }


# --------------------------------------------------------------
# 🔊 Endpoint: GET /audio/{filename}
# Serve the generated MP3 audio file to frontend
# --------------------------------------------------------------
@app.get("/audio/{filename}")
async def get_audio(filename: str):
    """
    Returns the MP3 audio file stored in backend/temp/.
    Frontend will use this URL to play the audio.
    """
    path = f"backend/temp/{filename}"

    # If file exists → return as audio/mpeg
    if os.path.exists(path):
        return FileResponse(path, media_type="audio/mpeg", filename=filename)

    # Error if file not found
    try:
       caption = caption_image_online(temp_path)
    except Exception as e:
       return {"error": f"Caption generation failed: {str(e)}"}

