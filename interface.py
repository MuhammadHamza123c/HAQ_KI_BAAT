import streamlit as st
import requests
import time

st.set_page_config(page_title="Haq ki Baat", layout="centered")

st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
        }
        img {
            margin-top: 40px;
            margin-bottom: 20px;
        }
        .response-box {
            background-color: #f1f1f1;
            padding: 20px;
            border-radius: 20px;
            max-height: 300px;
            overflow-y: auto;
            font-size: 19px;
            line-height: 1.8;
            color: #222;
        }
        .stChatInput {
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo.png", use_container_width=True)

prompt = st.chat_input(placeholder='Write down PAK LAW related query here!')

if prompt:
    with st.spinner("Thinking..."):
        time.sleep(3)
        url = f'https://359d0b28e537.ngrok-free.app/haq_ki_baat?query={prompt}'
        response = requests.get(url)
        data = response.json()
        st.markdown(f"<div class='response-box'>{data['Response']}</div>", unsafe_allow_html=True)
