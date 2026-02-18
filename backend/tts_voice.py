# ==============================================================
# 📁 backend/tts_voice.py
# Free Text → Speech (TTS) generation using gTTS
# ==============================================================

from gtts import gTTS
import os
import uuid
import logging   # ✅ Added logging


def generate_voice(text: str) -> str:
    """
    Converts text into speech (MP3) using gTTS.
    Returns the output file path.
    """

    # --------------------------------------------------------------
    # 🛑 Validate input
    # --------------------------------------------------------------
    if not text or text.strip() == "":
        raise ValueError("Text for TTS is empty.")

    # --------------------------------------------------------------
    # 📁 Create output directory
    # --------------------------------------------------------------
    output_dir = "backend/temp"
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, f"{uuid.uuid4()}.mp3")

    # --------------------------------------------------------------
    # 🎤 Generate speech audio
    # --------------------------------------------------------------
    try:
        tts = gTTS(text=text, lang="en")
        tts.save(file_path)

        logging.info(f"🔊 Audio generated at: {file_path}")

        # OLD VERSION
        # print(f"🔊 [TTS] Audio generated at: {file_path}")

        return file_path

    except Exception as e:
        logging.error(f"❌ TTS generation failed: {e}")

        # Optional: delete partial file if created
        if os.path.exists(file_path):
            os.remove(file_path)

        return "Error generating voice."
