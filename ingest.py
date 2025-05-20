import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from utils import extract_text_from_pdf, crawl_angelone_support
from dotenv import load_dotenv

load_dotenv()

def ingest_data():
    docs = []

    for fname in os.listdir("data/insurance_pdfs"):
        if fname.endswith(".pdf"):
            text = extract_text_from_pdf(os.path.join("data/insurance_pdfs", fname))
            docs.append(Document(page_content=text, metadata={"source": fname}))
    print('Documented PDFs')
    
    web_docs = crawl_angelone_support()
    print(f'Web Docs :: {web_docs}')
    print('Documented Webpage')

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    print('Chunked Data')

    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(chunks, embeddings)
    print(f'Indexed Vectors')
    vectordb.save_local("vectorstore")
