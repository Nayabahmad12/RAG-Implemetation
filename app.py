
from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.retriever import retrieve_documents
from src.llm import get_llm
from src.answer_generator import generate_answer


def main():

    print("Loading PDF documents...")
    documents = load_documents()
    print("Total pages:", len(documents))

    print("\nSplitting documents...")
    chunks = split_documents(documents)
    print("Total chunks:", len(chunks))

    print("\nCreating vector database...")
    vector_store = create_vector_store(chunks)

    print("\nLoading LLM...")
    llm = get_llm()

    print("\nPDF RAG Chatbot is ready!")

    while True:

        question = input("\nAsk your question (exit to stop): ")

        if question.lower() == "exit":
            break

        results = retrieve_documents(vector_store, question)

        answer = generate_answer(llm, question, results)

        print("\nAnswer:\n")
        print(answer)


if __name__ == "__main__":
    main()
