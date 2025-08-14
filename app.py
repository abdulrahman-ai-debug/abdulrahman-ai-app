    import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Abdulrahman.ai", layout="centered")
st.title("🎥 Abdulrahman.ai — Cinematic AI Studio by Hafiz Hammad Hussain")
st.markdown("##### تخیل کو حقیقت میں بدلیں — AI کے ذریعے")

# 🎨 Text-to-Image (Replicate)
st.subheader("🎨 تصویر بنائیں")
prompt_img = st.text_input("تصویر کے لیے خیال لکھیں:")
if st.button("تصویر بنائیں"):
    with st.spinner("تصویر بن رہی ہے..."):
        response = requests.post(
            "https://api.replicate.com/v1/predictions",
            headers={
                "Authorization": f"Token {os.getenv('REPLICATE_API_KEY')}",
                "Content-Type": "application/json"
            },
            json={
                "version": "a9758cb8b0c7...",  # Replace with actual version
                "input": {"prompt": prompt_img}
            }
        )
        if response.status_code == 201:
            get_url = response.json()["urls"]["get"]
            st.image(get_url, caption="Abdulrahman.ai Output")
        else:
            st.error("تصویر نہیں بن سکی")

# 🔊 Text-to-Speech (ElevenLabs)
st.subheader("🔊 آواز بنائیں")
text_voice = st.text_area("آواز کے لیے متن لکھیں:")
if st.button("آواز سنیں"):
    response = requests.post(
        "https://api.elevenlabs.io/v1/text-to-speech/voice_id",
        headers={"xi-api-key": os.getenv("ELEVEN_API_KEY")},
        json={"text": text_voice}
    )
    if response.ok:
        st.audio(response.content)
    else:
        st.error("آواز نہیں بن سکی")

# 🗣 Urdu TTS (Google TTS)
st.subheader("🗣 اردو آواز")
urdu_text = st.text_area("اردو میں کچھ لکھیں:")
if st.button("اردو آواز سنیں"):
    from gtts import gTTS
    tts = gTTS(text=urdu_text, lang='ur')
    tts.save("urdu_voice.mp3")
    audio_file = open("urdu_voice.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")

# 💬 GPT-4 Chatbot
st.subheader("💬 Abdulrahman Chatbot")
chat_input = st.text_input("سوال یا بات لکھیں:")
if st.button("جواب حاصل کریں"):
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4",
            "messages": [{"role": "user", "content": chat_input}]
        }
    )
    if response.ok:
        reply = response.json()["choices"][0]["message"]["content"]
        st.success(reply)
    else:
        st.error("جواب نہیں مل سکا")

st.markdown("---")
st.markdown("© Hafiz Hammad Hussain — Abdulrahman.ai")
