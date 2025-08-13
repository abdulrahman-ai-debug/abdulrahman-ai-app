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
