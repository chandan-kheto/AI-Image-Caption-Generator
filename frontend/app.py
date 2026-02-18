# ==============================================================
# 📁 frontend/app.py
# Streamlit Frontend for AI Image Caption + Voice Generator
# ==============================================================

import streamlit as st
import requests, os


# --------------------------------------------------------------
# 🌐 Backend API Base URL
# --------------------------------------------------------------
API_URL = "http://127.0.0.1:8000"


# --------------------------------------------------------------
# 🎨 Page Config
# --------------------------------------------------------------
st.set_page_config(
    page_title="AI Image Caption + Voice",
    layout="centered"
)

st.title("🖼️🎤 AI Image Caption + Voice Generator (free version)")
st.write("Upload an image — the AI will describe it and speak the caption aloud!")


# --------------------------------------------------------------
# 🧠 Session State Setup
# --------------------------------------------------------------
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None


# --------------------------------------------------------------
# 📸 File Uploader
# --------------------------------------------------------------
uploaded = st.file_uploader(
    "📸 Upload an image",
    type=["jpg", "jpeg", "png", "webp"],
    key="file_uploader"
)

# Save uploaded file to session state
if uploaded:
    st.session_state.uploaded_file = uploaded


# --------------------------------------------------------------
# 🖼 Image Preview
# --------------------------------------------------------------
if st.session_state.uploaded_file:
    st.image(st.session_state.uploaded_file,
             caption="Uploaded Image",
             use_container_width=True)


# --------------------------------------------------------------
# ✨ Buttons (ALWAYS VISIBLE)
# --------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    generate = st.button(
        "✨ Generate Caption + Voice",
        disabled=st.session_state.uploaded_file is None
    )

with col2:
    clear = st.button("🧹Clear chat")


# --------------------------------------------------------------
# 🗑 Clear Logic
# --------------------------------------------------------------
if clear:
    st.session_state.uploaded_file = None
    st.session_state.file_uploader = None
    st.rerun()


# --------------------------------------------------------------
# ✨ Generate Logic
# --------------------------------------------------------------
if generate and st.session_state.uploaded_file:

    file = st.session_state.uploaded_file

    files = {
        "file": (file.name, file.getvalue(), file.type)
    }

    with st.spinner("Generating caption and voice... ⏳"):
        resp = requests.post(f"{API_URL}/caption/online", files=files)

    if resp.status_code == 200:
        data = resp.json()

        st.success("✅ Caption Generated:")
        st.write(data["caption"])

        audio_path = data["voice_path"]
        audio_filename = os.path.basename(audio_path)
        audio_url = f"{API_URL}/audio/{audio_filename}"

        st.audio(audio_url)

    else:
        st.error("❌ Something went wrong. Please try again.")
