# ==============================================================
# 📁 backend/main.py
# FastAPI backend for AI Image Caption + Voice Generator (Free)
# ==============================================================

from pathlib import Path
from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from backend.caption_gen_openrouter import caption_image_online
from backend.tts_voice import generate_voice
import os, uuid

app = FastAPI(title="AI Image Caption + Voice Generator (Free)")

# ✅ Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("backend/temp", exist_ok=True)

@app.post("/caption/online")
async def caption_online(file: UploadFile = File(...)):
    """
    Upload image → Generate caption via OpenRouter → Convert caption to voice
    """
    image_bytes = await file.read()
    ext = os.path.splitext(file.filename)[1] or ".jpg"
    temp_path = f"backend/temp/{uuid.uuid4()}{ext}"

    with open(temp_path, "wb") as f:
        f.write(image_bytes)

    caption = caption_image_online(temp_path)
    os.remove(temp_path)

    voice_path = generate_voice(caption)
    return {"caption": caption, "voice_path": voice_path}


@app.get("/audio/{filename}")
async def get_audio(filename: str):
    path = f"backend/temp/{filename}"
    if os.path.exists(path):
        return FileResponse(path, media_type="audio/mpeg", filename=filename)
    return {"error": "File not found"}
