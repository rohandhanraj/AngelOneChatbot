from langgraph.graph import StateGraph
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from schema import GraphState
from dotenv import load_dotenv
load_dotenv()

def get_rag_graph():
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    vectordb = FAISS.load_local("vectorstore", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    workflow = StateGraph(GraphState)

    def retrieve(state):
        docs = retriever.get_relevant_documents(state["question"])
        return {"question": state["question"], "docs": docs}

    def generate(state):
        docs = state["docs"]
        if not docs:
            return {"answer": "I don't know."}
        context = "\n".join([doc.page_content for doc in docs])
        prompt = f"Answer the question using the context below. If the answer is not present, say 'I don't know'.\n\nContext:\n{context}\n\nQuestion:\n{state['question']}"
        result = llm.invoke(prompt)
        return {"answer": result.content}

    workflow.add_node("retrieve", retrieve)
    workflow.add_node("generate", generate)

    workflow.set_entry_point("retrieve")
    workflow.add_edge("retrieve", "generate")

    graph = workflow.compile()
    return graph