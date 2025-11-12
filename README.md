🖼️🎤 AI Image Caption + Voice Generator (Free Version)
🚀 Overview

AI Image Caption + Voice Generator is a free and open-source app that uses AI vision models to describe any image and then speaks the caption aloud using text-to-speech.

It combines:

🧠 OpenRouter (GPT-4o-mini) for smart image-to-text captioning

🎤 Google TTS (gTTS) for realistic voice output

⚙️ FastAPI backend

💻 Streamlit frontend

Everything runs 100% free — no paid APIs required!

🎯 Features

✅ Upload any image (JPG, PNG, WEBP)
✅ Generates a meaningful one-line caption using AI
✅ Converts the caption into an MP3 voice automatically
✅ Simple, clean Streamlit interface
✅ Built entirely with open and free technologies

🧠 Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	FastAPI
AI Model	OpenRouter (gpt-4o-mini)
Text-to-Speech	gTTS (Google Text-to-Speech)
Environment	Python + dotenv
Communication	REST API (JSON)

🏗️ Project Structure
AI Image Caption Generator/
│
├── backend/
│   ├── main.py
│   ├── caption_gen_openrouter.py
│   ├── tts_voice.py
│   ├── __init__.py
│   └── temp/
│
├── app.py
│
├── .env
└── requirements.txt

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/ai-image-caption-voice-generator.git
cd ai-image-caption-voice-generator

2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate  # (Windows)
# or
source venv/bin/activate  # (Mac/Linux)

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Your .env File

Create a file named .env in the root directory and paste:

OPENROUTER_API_KEY=your_openrouter_api_key_here
MODEL=openai/gpt-4o-mini


🧩 Get your free key from OpenRouter.ai

5️⃣ Start the Backend
uvicorn backend.main:app --reload


Visit 👉 http://127.0.0.1:8000/docs
 to test endpoints.

6️⃣ Start the Frontend

In a new terminal:

cd frontend
streamlit run app.py


Your app will open at 👉 http://localhost:8501

🧩 Example Output
Image Input	AI Caption	Voice Output
🖼️ Eiffel Tower	“A beautiful view of the Eiffel Tower against a clear blue sky.”	🔊 Spoken via gTTS
🐶 Dog	“A happy golden retriever playing on green grass.”	🔊 Spoken via gTTS
🌇 City Sunset	“A breathtaking sunset illuminating the modern city skyline.”	🔊 Spoken via gTTS

📦 Requirements
fastapi
uvicorn
requests
gtts
python-dotenv
streamlit
python-multipart

🧠 How It Works

User uploads an image on the Streamlit UI

Image is sent to the FastAPI backend

The backend sends the image (base64 encoded) to OpenRouter

The LLM generates a natural English caption

Caption text is passed to gTTS

The app returns the caption and the generated voice file

🛠️ Future Improvements

🎙️ Add custom voice styles (ElevenLabs API)

🖋️ Allow multiple caption styles (short, funny, poetic)

🧱 Add database for storing past captions

🌐 Deploy on Render / Hugging Face Spaces

🧑‍💻 Author: Chandan Kheto
🚀 AI Developer
🌟 Support
If you found this project useful, please ⭐ the repo — it motivates continued updates!
