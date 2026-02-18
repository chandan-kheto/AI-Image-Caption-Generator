# ==============================================================
# 📁 backend/caption_gen_openrouter.py
# Online Image → Text Captioning using OpenRouter API
# ==============================================================

from pathlib import Path
from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

import requests, base64, os, mimetypes
import logging   # ✅ Added proper logging


def caption_image_online(image_path: str) -> str:
    """
    Sends an image to OpenRouter API and returns a generated caption.
    """

    # --------------------------------------------------------------
    # 🔑 Load API Key + Model from .env
    # --------------------------------------------------------------
    API_KEY = os.getenv("OPENROUTER_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-4o-mini")

    if not API_KEY:
        raise ValueError("❌ OPENROUTER_API_KEY not found in environment")

    # --------------------------------------------------------------
    # 📸 Convert image to base64
    # --------------------------------------------------------------
    with open(image_path, "rb") as f:
        img_base64 = base64.b64encode(f.read()).decode("utf-8")

    mime = mimetypes.guess_type(image_path)[0] or "image/jpeg"

    # --------------------------------------------------------------
    # 🌐 OpenRouter API Endpoint
    # --------------------------------------------------------------
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
                    {"type": "text",
                     "text": "Describe this image in one clear, short, beautiful English sentence."},

                    {"type": "image_url",
                     "image_url": f"data:{mime};base64,{img_base64}"}
                ],
            }
        ],
    }

    # --------------------------------------------------------------
    # 🚀 Send POST Request (with timeout added)
    # --------------------------------------------------------------
    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=30   # ✅ Added timeout (important)
        )

        # OLD VERSION (without timeout)
        # response = requests.post(url, headers=headers, json=data)

    except requests.exceptions.Timeout:
        logging.error("❌ OpenRouter request timed out")
        return "Caption service is taking too long. Please try again."

    except requests.exceptions.RequestException as e:
        logging.error(f"❌ Request failed: {e}")
        return "Failed to connect to caption service."

    # --------------------------------------------------------------
    # ✅ SUCCESS → Extract caption
    # --------------------------------------------------------------
    if response.status_code == 200:
        try:
            caption = response.json()["choices"][0]["message"]["content"]
            logging.info(f"🖼️ Caption Generated: {caption}")

            # OLD PRINT VERSION
            # print(f"🖼️ [CaptionGen] {caption}")

            return caption

        except Exception as e:
            logging.error(f"❌ JSON Parse Error: {e}")
            logging.error(f"Response: {response.text}")

            # OLD VERSION
            # print("❌ [Parse Error]:", e)
            # print("Response:", response.text)

            return "Error parsing caption response."

    # --------------------------------------------------------------
    # ❌ FAILURE → Clean Error Message
    # --------------------------------------------------------------
    else:
        logging.error(f"❌ API Error: {response.status_code} - {response.text}")

        # OLD VERSION (exposed raw API response)
        # return f"Error: {response.status_code} - {response.text}"

        return "Failed to generate caption. Please try again."
