import streamlit as st
import requests
import asyncio

# Ensure async works in Streamlit
try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from BLL.ai_processor import generate_response

# Backend API URL
API_URL = "http://127.0.0.1:8000/ask"

# Streamlit UI
st.title("🧠 GraphRAG AI Q&A")

query = st.text_input("Ask a question:")
if st.button("Get Answer"):
    if not query:
        st.warning("⚠️ Please enter a question!")
    else:
        response = requests.get(API_URL, params={"query": query}).json()
        answer = generate_response(response)
        st.write(answer)
