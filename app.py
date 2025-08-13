import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# 🎬 Logo + Corner Image
logo_url = "https://your-uploaded-url.com/logo.png"  # ← Replace with your logo URL
corner_url = "https://your-uploaded-url.com/corner.jpg"  # ← Replace with your corner image URL

st.image(logo_url, width=100)
st.image(corner_url, caption="Hafiz Hammad Hussain", width=250)

st.title("🎬 Abdulrahman.ai — Cinematic AI Studio")
st.markdown("---")

# 🔐 Password Gate
password = st.text_input("🔐 Please enter password", type="password")
if password != "Okara":
    st.warning("🔒 Access Denied. Please enter correct password.")
    st.stop()

# 🎥 Feature Selection
st.subheader("🎯 Choose Your Cinematic Tool")
tool = st.selectbox("Select a feature", [
    "🖼️ Text to Image",
    "📹 Text to Video",
    "🎤 Text to Voice",
    "🎶 Text to Song",
    "👄 Lip Sync",
    "🧑‍🎤 Animate Photo"
])

st.markdown("---")

# 🖼️ Text to Image
if tool == "🖼️ Text to Image":
    st.subheader("🖼️ Text to Image Generator")
    style = st.selectbox("Choose style", ["Cartoon", "Realistic", "3D", "Steampunk", "Oil Painting", "Vintage", "Viral Kids"])
    ratio = st.selectbox("Choose ratio", ["1:1", "16:9", "9:16"])
    prompt = st.text_area("Enter your image prompt")
    if st.button("🚀 Generate Image"):
        st.success(f"Generated {style} image with {ratio} ratio.")
        st.image("https://via.placeholder.com/512x512.png", caption="Preview")
        st.download_button("📥 Download", "Image content", file_name="image.png")
        st.button("🔗 Share")

# 📹 Text to Video
elif tool == "📹 Text to Video":
    st.subheader("📹 Text to Video Generator")
    style = st.selectbox("Choose video style", ["Realistic", "Anime", "Cinematic", "Cartoon"])
    duration = st.slider("Select duration (minutes)", 1, 30, 5)
    frames = st.slider("Select frame count", 10, 1000, 100)
    prompt = st.text_area("Enter your video prompt")
    if st.button("🎬 Generate Video"):
        st.success(f"{duration}-minute {style} video with {frames} frames generated.")
        st.video("https://sample-videos.com/video123.mp4")
        st.download_button("📥 Download", "Video content", file_name="video.mp4")
        st.button("🔗 Share")

# 🎤 Text to Voice
elif tool == "🎤 Text to Voice":
    st.subheader("🎤 Text to Voice Generator")
    voice_type = st.selectbox("Choose voice type", ["Child", "Adult", "Cartoon", "Old"])
    accent = st.selectbox("Choose accent", ["US English", "UK English", "Urdu"])
    emotion = st.selectbox("Choose emotion", ["Happy", "Sad", "Angry", "Neutral"])
    text = st.text_area("Enter text to convert to voice")
    if st.button("🔊 Generate Voice"):
        st.success(f"{voice_type} voice with {accent} accent and {emotion} emotion generated.")
        st.audio("https://sample-videos.com/audio123.mp3")
        st.download_button("📥 Download", "Voice content", file_name="voice.mp3")
        st.button("🔗 Share")

# 🎶 Text to Song
elif tool == "🎶 Text to Song":
    st.subheader("🎶 Text to Song Generator")
    genre = st.selectbox("Choose genre", ["Rap", "Sad", "Happy", "Classical", "Pop"])
    language = st.selectbox("Choose language", ["English", "Urdu"])
    style = st.selectbox("Choose style", ["Suno Style", "Udio Style", "Custom"])
    lyrics = st.text_area("Enter your lyrics")
    if st.button("🎵 Generate Song"):
        st.success(f"{genre} song in {language} using {style} style generated.")
        st.audio("https://sample-videos.com/audio123.mp3")
        st.download_button("📥 Download", "Song content", file_name="song.mp3")
        st.button("🔗 Share")

# 👄 Lip Sync
elif tool == "👄 Lip Sync":
    st.subheader("👄 Lip Sync Generator")
    uploaded_photo = st.file_uploader("Upload photo")
    uploaded_voice = st.file_uploader("Upload voice")
    speed = st.slider("Lip sync speed", 0.5, 2.0, 1.0)
    if st.button("🎭 Generate Lip Sync"):
        st.success("Lip sync video generated.")
        st.video("https://sample-videos.com/video123.mp4")
        st.download_button("📥 Download", "LipSync content", file_name="lipsync.mp4")
        st.button("🔗 Share")

# 🧑‍🎤 Animate Photo
elif tool == "🧑‍🎤 Animate Photo":
    st.subheader("🧑‍🎤 Animate Photo")
    animation_type = st.selectbox("Choose animation", ["Ripple", "3D Zoom", "Cinemagraph", "Sparkle"])
    overlay = st.selectbox("Choose overlay", ["Rain", "Fire", "Glow", "None"])
    uploaded_image = st.file_uploader("Upload photo to animate")
    if st.button("✨ Animate"):
        st.success(f"{animation_type} animation with {overlay} overlay applied.")
        st.image("https://via.placeholder.com/512x512.png", caption="Animated Preview")
        st.download_button("📥 Download", "Animation content", file_name="animated.gif")
        st.button("🔗 Share")

# 📁 Saved Projects
st.markdown("---")
st.subheader("📁 Saved Projects")
st.info("🧠 The projects you have worked on are saved here for future access.")

# 🧾 Footer Branding
st.markdown("---")
st.markdown("**Created by Hafiz Hammad Hussain — Founder of Abdulrahman.ai**")
