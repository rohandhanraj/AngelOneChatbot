import streamlit as st
from langgraph_rag import get_rag_graph
import os
from ingest import ingest_data
import logging


logging_str = "[%(asctime)s: %(levelname)s: %(module)s] %(message)s"
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename = os.path.join(log_dir,'running_logs.log'), level=logging.INFO, format=logging_str)

if not os.path.exists("vectorstore/index.faiss"):
    ingest_data()

st.set_page_config(page_title="Angel One Chatbot", layout="centered")
st.title("📊 Angel One Support Assistant")
st.caption("Ask questions based on Angel One support & insurance documents.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

graph = get_rag_graph()

query = st.text_input("Enter your question:", key="user_input")

if st.button("Ask"):
    if query:
        result = graph.invoke({"question": query})
        answer = result.get("answer", "I don't know.")
        st.session_state.chat_history.append((query, answer))

for q, a in reversed(st.session_state.chat_history):
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Bot:** {a}")