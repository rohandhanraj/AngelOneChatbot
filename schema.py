from typing import TypedDict, List
from langchain.schema import Document

class GraphState(TypedDict):
    question: str
    docs: List[Document]
    answer: str