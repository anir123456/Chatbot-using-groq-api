from langchain_groq import ChatGroq
import streamlit as st
import os
from dotenv import load_dotenv


load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

if not groq_api_key:
    st.error("❌ GROQ_API_KEY is missing. Set it in .env file.")
    st.stop()


llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")


st.title("🤖 Myself Anirban")
st.markdown("Ask me anything you want")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="user_input")

if user_input:
    st.session_state.chat_history.append(("You", user_input))
    try:
        response = llm.invoke(user_input)
        st.session_state.chat_history.append(("Groq", response.content))
    except Exception as e:
        st.session_state.chat_history.append(("Groq", f"⚠️ Error: {e}"))

for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {msg}")
