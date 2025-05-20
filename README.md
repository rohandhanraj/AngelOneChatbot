# 📊 Angel One RAG Chatbot

This is a Retrieval-Augmented Generation (RAG) chatbot that answers questions using Angel One customer support documentation and insurance PDFs. It uses LangGraph for pipeline control and Streamlit as the frontend.

## 🧠 Features

- LangGraph-powered RAG flow
- Answers ONLY from provided data
- Replies "I don't know" when answer is not in source
- Clean Streamlit UI
- Free deployment support

## 📁 Sources

- Angel One: https://www.angelone.in/support
- Insurance PDFs in `data/insurance_pdfs/`

---


## 📁 Project Structure

```
rag-chatbot/
├── app.py                     # Streamlit app
├── ingest.py                 # Index support docs + PDFs into FAISS
├── langgraph_rag.py          # LangGraph RAG pipeline
├── utils.py                  # PDF & web crawler helpers
├── requirements.txt
├── README.md
├── .env
├── data/
│   ├── insurance_pdfs/
│   └── support_docs/
├── vectorstore/
```
---


## 🔧 Setup Instructions

1. **Clone the Repo**
   ```bash
   git clone https://github.com/your-username/rag-chatbot.git
   cd rag-chatbot
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add OpenAI Key**
   - Create `.env`:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

4. **Run the App**
   ```bash
   streamlit run app.py
   ```

## 🚀 Deploy for Free

### Hugging Face Spaces
1. Go to https://huggingface.co/spaces
2. Create new Space → Choose **Streamlit**
3. Upload all files
4. Add `OPENAI_API_KEY` in **Secrets**

### Render.com
1. Go to https://render.com/
2. New → Web Service
3. Connect GitHub repo
4. Runtime: Python
5. Start command:
   ```bash
   streamlit run app.py --server.port=10000
   ```
