🖼️🎤 AI Image Caption + Voice Generator (Free Version)

Generate smart AI captions from any image and convert them into natural voice — 100% free, using open-source APIs.

🚀 Overview

AI Image Caption + Voice Generator is a lightweight, free, and open-source AI application that:

🧠 Describes any image using OpenRouter (GPT-4o-mini)

🎤 Speaks the caption out loud using gTTS (Google Text-to-Speech)

⚙️ Runs on a FastAPI backend

💻 Has a clean Streamlit frontend

💰 Uses only free APIs, no paid credits required

🎯 Features

✅ Upload any image (JPG, PNG, WEBP)
✅ AI generates a meaningful one-line caption
✅ gTTS converts caption into a downloadable MP3 file
✅ Clean & modern Streamlit UI
✅ FastAPI backend with REST API
✅ No GPU required — works on any laptop

🧠 Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	FastAPI
Image Captioning	GPT-4o-mini (OpenRouter)
Voice Output	gTTS (Google TTS)
Environment	Python + dotenv
Communication	REST API (JSON)
🏗️ Project Structure
AI-Image-Caption-Voice-Generator/
│
├── backend/
│   ├── main.py                   # FastAPI app
│   ├── caption_gen_openrouter.py # Image → Caption
│   ├── tts_voice.py              # Caption → Voice
│   ├── __init__.py
│   └── temp/                     # Stores uploaded images + mp3
│
├── frontend/
│   └── app.py                    # Streamlit UI
│
├── .env                          # API keys (ignored in Git)
└── requirements.txt

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/ai-image-caption-voice-generator.git
cd ai-image-caption-voice-generator

2️⃣ Create a Virtual Environment
Windows:
python -m venv venv
venv\Scripts\activate

Mac / Linux:
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Your .env File

Create a file named .env in the project root:

OPENROUTER_API_KEY=your_openrouter_api_key_here
MODEL=openai/gpt-4o-mini


🌐 Get your free API key → https://openrouter.ai

5️⃣ Start the Backend (FastAPI)
uvicorn backend.main:app --reload


Then visit:

👉 http://127.0.0.1:8000/docs

(API testing with Swagger UI)

6️⃣ Start the Frontend (Streamlit)
cd frontend
streamlit run app.py


Your UI opens at:

👉 http://localhost:8501

🧩 Example Outputs
Image Input	AI Caption	Voice Output
🗼 Eiffel Tower	“A beautiful view of the Eiffel Tower against a blue sky.”	🔊 MP3 via gTTS
🐶 Golden Retriever	“A happy golden retriever playing on green grass.”	🔊 MP3 via gTTS
🌇 City Sunset	“A breathtaking sunset illuminating the city skyline.”	🔊 MP3 via gTTS
📦 Requirements
fastapi
uvicorn
requests
gtts
python-dotenv
streamlit
python-multipart

🧠 How It Works (Flow)

User uploads an image via Streamlit

Image is sent to FastAPI (base64 encoded)

Backend sends prompt + image to OpenRouter

LLM generates a natural English caption

Caption is passed to gTTS → MP3 file generated

Streamlit displays caption + plays audio

🛠️ Future Improvements

🔊 Add multiple voice styles (ElevenLabs API)
📜 Provide different caption modes (funny, poetic, detailed)
🧱 Add a database to store past captions
🚀 Deploy on Render, HuggingFace Spaces, or Vercel

👤 Author

Chandan Kheto
🚀 AI Developer
⭐ If you like this project, please give the repo a star — it motivates me to build more!
