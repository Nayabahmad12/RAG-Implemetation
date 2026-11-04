
import streamlit as st
import os
import shutil

from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.retriever import retrieve_documents
from src.llm import get_llm
from src.answer_generator import generate_answer


st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="📚",
    layout="wide"
)

st.title("📚 PDF RAG Chatbot")
st.write("Upload your PDFs and ask questions about their content.")

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "llm" not in st.session_state:
    st.session_state.llm = None

if "messages" not in st.session_state:
    st.session_state.messages = []


with st.sidebar:

    st.header("Upload PDF Documents")

    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button("Create Knowledge Base"):

        if not uploaded_files:
            st.warning("Please upload at least one PDF.")

        else:

            folder_path = "data/pdf"
            os.makedirs(folder_path, exist_ok=True)

            for filename in os.listdir(folder_path):
                if filename.lower().endswith(".pdf"):
                    os.remove(os.path.join(folder_path, filename))

            for file in uploaded_files:

                file_path = os.path.join(folder_path, file.name)

                with open(file_path, "wb") as f:
                    f.write(file.getbuffer())

            with st.spinner("Processing PDF documents..."):

                if os.path.exists("chroma_db"):
                    shutil.rmtree("chroma_db")

                documents = load_documents()

                chunks = split_documents(documents)

                vector_store = create_vector_store(chunks)

                st.session_state.vector_store = vector_store
                st.session_state.llm = get_llm()
                st.session_state.messages = []

            st.success("Knowledge base created successfully!")


    if st.button("Clear Chat"):
        st.session_state.messages = []


if st.session_state.vector_store is None:

    st.info("Upload PDF files and create your knowledge base to start chatting.")

else:

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Ask something about your PDFs...")

    if question:

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):

            with st.spinner("Searching your PDFs and generating answer..."):

                results = retrieve_documents(
                    st.session_state.vector_store,
                    question
                )

                answer = generate_answer(
                    st.session_state.llm,
                    question,
                    results
                )

                st.markdown(answer)

                with st.expander("View retrieved PDF sources"):

                    for i, doc in enumerate(results):

                        source = os.path.basename(
                            doc.metadata.get("source", "Unknown")
                        )

                        page = doc.metadata.get("page", 0) + 1

                        st.write(f"**Source {i+1}: {source}**")
                        st.write(f"Page: {page}")
                        st.write(doc.page_content)
                        st.divider()

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })
