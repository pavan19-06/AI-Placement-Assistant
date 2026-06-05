from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
from pypdf import PdfReader

documents = []

for file in os.listdir("documents"):
    if file.endswith(".pdf"):
        pdf = PdfReader(f"documents/{file}")

        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""

        documents.append(text)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = []

for doc in documents:
    chunks.extend(splitter.split_text(doc))

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.from_texts(chunks, embeddings)

db.save_local("vector_db")

print("Vector DB created successfully!")