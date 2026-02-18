# ==============================================================
# 📁 backend/caption_gen_openrouter.py
# Online Image → Text Captioning using OpenRouter API
# ==============================================================

from pathlib import Path
from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

import requests
import base64
import os
import mimetypes

def caption_image_online(image_path: str) -> str:
    """
    Sends an image to OpenRouter API and returns a generated caption.
    """
    API_KEY = os.getenv("OPENROUTER_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-4o-mini")

    if not API_KEY:
        raise ValueError("❌ OPENROUTER_API_KEY not found in environment")

    with open(image_path, "rb") as f:
        img_base64 = base64.b64encode(f.read()).decode("utf-8")

    mime = mimetypes.guess_type(image_path)[0] or "image/jpeg"

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image in one clear, short, beautiful English sentence."},
                    {"type": "image_url", "image_url": f"data:{mime};base64,{img_base64}"}
                ],
            }
        ],
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        try:
            caption = response.json()["choices"][0]["message"]["content"]
            print(f"🖼️ [CaptionGen] {caption}")
            return caption
        except Exception as e:
            print("❌ [Parse Error]:", e)
            print("Response:", response.text)
            return "Error parsing caption response."
    else:
        print(f"❌ [API Error]: {response.status_code} - {response.text}")
        return f"Error: {response.status_code} - {response.text}"
