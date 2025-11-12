# ==============================================================
# 📁 frontend/app.py
# Streamlit Frontend for AI Image Caption + Voice Generator
# ==============================================================

import streamlit as st
import requests
import os

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Image Caption + Voice", page_icon="🎤", layout="centered")
st.title("🖼️🎤 AI Image Caption + Voice Generator (Free Version)")
st.write("Upload an image — the AI will describe it and speak the caption aloud!")

uploaded = st.file_uploader("📸 Upload an image", type=["jpg", "jpeg", "png", "webp"])

if uploaded:
    st.image(uploaded, caption="Uploaded Image", width="stretch")

if uploaded and st.button("✨ Generate Caption + Voice"):
    files = {"file": (uploaded.name, uploaded.getvalue(), uploaded.type)}

    with st.spinner("Generating caption and voice... ⏳"):
        resp = requests.post(f"{API_URL}/caption/online", files=files)

    if resp.status_code == 200:
        data = resp.json()
        st.success("✅ Caption Generated:")
        st.write(data["caption"])

        # Audio playback
        audio_path = data["voice_path"]
        audio_filename = os.path.basename(audio_path)
        audio_url = f"{API_URL}/audio/{audio_filename}"
        st.audio(audio_url)
    else:
        st.error("❌ Something went wrong. Please try again.")
