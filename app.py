import streamlit as st

# Set page config
st.set_page_config(page_title="Abdulrahman.ai", layout="centered")

# Define your password
correct_password = "Okara"

# Session state to track login
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Password gate
if not st.session_state.authenticated:
    st.title("🔐 Abdulrahman.ai Access")
    password_input = st.text_input("Please enter password here:", type="password")
    if st.button("Enter"):
        if password_input == correct_password:
            st.session_state.authenticated = True
            st.success("Welcome! 🎬")
        else:
            st.error("Incorrect password. Access denied.")
else:
    # Main App Interface
    st.title("🎬 Welcome to Abdulrahman.ai")
    st.subheader("Choose your cinematic tool:")
# 🎬 Hafiz Hammad Hussain — Cinematic Header
from PIL import Image
import requests
from io import BytesIO

corner_image_url = "https://your-uploaded-url.com/hammad-corner.jpg"  # ← Replace with actual corner image URL
response = requests.get(corner_image_url)
corner_img = Image.open(BytesIO(response.content))
st.image(corner_img, caption="Hafiz Hammad Hussain", width=250)

st.title("🎬 Abdulrahman.ai — Cinematic AI Studio")
st.markdown("---")

# 🔐 Password Gate
password = st.text_input("🔐 Please enter password here", type="password")
if password != "Okara":
    st.warning("🔒 Access Denied. Please enter correct password.")
    st.stop()

# 🎬 Cinematic Feature Boxes
st.markdown("## 🎥 Choose Your Cinematic Tool")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://your-uploaded-url.com/text-to-image.jpg", width=150)  # ← Text to Image
    if st.button("🖼️ Text to Image"):
        st.session_state.tool = "image"

with col2:
    st.image("https://your-uploaded-url.com/text-to-video.jpg", width=150)  # ← Text to Video
    if st.button("📹 Text to Video"):
        st.session_state.tool = "video"

with col3:
    st.image("https://your-uploaded-url.com/text-to-voice.jpg", width=150)  # ← Text to Voice
    if st.button("🎤 Text to Voice"):
        st.session_state.tool = "voice"

col4, col5, col6 = st.columns(3)

with col4:
    st.image("https://your-uploaded-url.com/text-to-song.jpg", width=150)  # ← Text to Song
    if st.button("🎶 Text to Song"):
        st.session_state.tool = "song"

with col5:
    st.image("https://your-uploaded-url.com/lip-sync.jpg", width=150)  # ← Lip Sync
    if st.button("👄 Lip Sync"):
        st.session_state.tool = "lipsync"

with col6:
    st.image("https://your-uploaded-url.com/animate-photo.jpg", width=150)  # ← Animate Photo
    if st.button("🧑‍🎤 Animate Photo"):
        st.session_state.tool = "animate"

st.markdown("---")

# 📥 Saved Projects Section
st.subheader("📁 Saved Projects")
st.info("🧠 The projects you have worked on are saved here for future access.")

# 🧠 Branded Footer
st.markdown("---")
st.markdown("**Created by Hafiz Hammad Hussain — Founder of Abdulrahman.ai**")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("Text to Image")
        st.button("Text to Video")
    with col2:
        st.button("Text to Voice")
        st.button("Photo Lip Sync")
    with col3:
        st.button("Text to Song")
        st.button("Animate Photo to Video")

    st.markdown("---")
    st.info("📁 The projects you have worked on are saved here.")
    st.caption("This cutting-edge AI tool, created by Hafiz Hammad Hussain, fulfills your needs with ease, speed, and accuracy.")
