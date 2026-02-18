

# ==============================================================
# 📁 frontend/app.py
# Streamlit Frontend for AI Image Caption + Voice Generator
# ==============================================================

# Streamlit UI framework
import streamlit as st

# To send image → backend
import requests

# For extracting filename from paths
import os


# --------------------------------------------------------------
# 🌐 Backend API Base URL
# --------------------------------------------------------------
API_URL = "http://127.0.0.1:8000"   # FastAPI backend running locally


# --------------------------------------------------------------
# 🎨 Streamlit Page Setup
# --------------------------------------------------------------
st.set_page_config(
    page_title="AI Image Caption + Voice",
    page_icon="🎤",
    layout="centered"
)

st.title("🖼️🎤 AI Image Caption + Voice Generator (Free Version)")
st.write("Upload an image — the AI will describe it and speak the caption aloud!")


# --------------------------------------------------------------
# 📸 Image Upload Component
# --------------------------------------------------------------
uploaded = st.file_uploader(
    "📸 Upload an image",
    type=["jpg", "jpeg", "png", "webp"]
)

# Preview uploaded image
if uploaded:
    st.image(uploaded, caption="Uploaded Image", width="stretch")


# --------------------------------------------------------------
# ✨ Main Button → Generate Caption + Voice
# --------------------------------------------------------------
if uploaded and st.button("✨ Generate Caption + Voice"):

    # Convert uploaded file for FastAPI
    files = {
        "file": (uploaded.name, uploaded.getvalue(), uploaded.type)
    }

    # Show loading spinner
    with st.spinner("Generating caption and voice... ⏳"):
        # Send POST request → backend
        resp = requests.post(f"{API_URL}/caption/online", files=files)

    # ----------------------------------------------------------
    # ✅ Success response (200 OK)
    # ----------------------------------------------------------
    if resp.status_code == 200:
        data = resp.json()

        # Show caption text
        st.success("✅ Caption Generated:")
        st.write(data["caption"])

        # ------------------------------------------------------
        # 🔊 Audio playback section
        # ------------------------------------------------------
        audio_path = data["voice_path"]           # ex: backend/temp/1234.mp3
        audio_filename = os.path.basename(audio_path)
        audio_url = f"{API_URL}/audio/{audio_filename}"

        # Streamlit audio player
        st.audio(audio_url)

    # ----------------------------------------------------------
    # ❌ Error handling
    # ----------------------------------------------------------
    else:
        st.error("❌ Something went wrong. Please try again.")
