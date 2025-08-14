    import openai
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import os
from dotenv import load_dotenv

# 🔐 Secure API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 🎨 Abdulrahman.ai UI
st.set_page_config(page_title="Abdulrahman.ai", layout="centered")
st.markdown("<h1 style='text-align: center; color: white;'>🎬 Abdulrahman.ai</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: gray;'>بسم اللّٰہ! AI سفر شروع ہو رہا ہے</h3>", unsafe_allow_html=True)

prompt = st.text_input("💡 اپنا خیال لکھیں (اردو یا انگریزی):")

if st.button("🔮 تصویر بنائیں"):
    if prompt:
        with st.spinner("تصویر بن رہی ہے..."):
            try:
                response = openai.Image.create(
                    prompt=prompt,
                    n=1,
                    size="512x512"
                )
                image_url = response['data'][0]['url']
                image_response = requests.get(image_url)
                img = Image.open(BytesIO(image_response.content))
                st.image(img, caption="✨ Abdulrahman.ai کی تخلیق", use_column_width=True)
                st.success("تصویر تیار ہے! 🎉")
            except Exception as e:
                st.error(f"کوئی مسئلہ آ گیا ہے: {e}")
    else:
        st.warning("براہ کرم کوئی خیال لکھیں تاکہ تصویر بن سکے۔")
