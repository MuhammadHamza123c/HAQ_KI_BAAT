import streamlit as st
import requests



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
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 15px;
            max-height: 300px;
            overflow-y: auto;
            font-size: 18px;
            line-height: 1.6;
            color: #222;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.image("logo.png", use_container_width=True)



uploaded_file = st.file_uploader("Upload Image or PDF (optional)", type=["pdf", "png", "jpg", "jpeg"])
query = st.chat_input(placeholder="✍️ Write your legal query here")
print(query)
if query or uploaded_file:
    with st.spinner("📡 Processing... please wait..."):
        try:
            # Prepare request
            files = {"f1": (uploaded_file.name, uploaded_file.getvalue())} if uploaded_file else None
            data = {"query": query}

            response = requests.post(
                "http://127.0.0.1:8000/upload_file_query",  # Replace with your FastAPI URL
                files=files,
                data=data
            )

            if response.status_code == 200:
                result = response.json()
                st.markdown(f"<div class='response-box'>{result['Response']}</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ Error: {response.status_code} — {response.text}")

        except Exception as e:
            st.error(f"❌ Exception: {e}")

else:
    st.info("⚠️ Please write a query or upload a file to begin.")
