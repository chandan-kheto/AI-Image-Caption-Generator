# ==============================================================
# 📁 backend/tts_voice.py
# Free Text → Speech (TTS) generation using gTTS
# ==============================================================

from gtts import gTTS
import os
import uuid

def generate_voice(text: str) -> str:
    """
    Converts text to speech using gTTS (Google Text-to-Speech)
    and saves it as an MP3 file.
    """
    if not text or text.strip() == "":
        raise ValueError("Text for TTS is empty.")

    output_dir = "backend/temp"
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, f"{uuid.uuid4()}.mp3")

    tts = gTTS(text=text, lang="en")
    tts.save(file_path)

    print(f"🔊 [TTS] Audio generated at: {file_path}")
    return file_path
