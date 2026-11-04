
import os

def generate_answer(llm, question, retrieved_docs):

    context = ""

    for i, doc in enumerate(retrieved_docs):

        source = os.path.basename(doc.metadata.get("source", "Unknown"))

        page = doc.metadata.get("page", 0) + 1

        context += f"""
        [Source {i+1}: {source}, Page {page}]

        {doc.page_content}

        """

    prompt = f"""
    You are a helpful PDF-based AI assistant.

    Answer the question using only the provided context.

    Instructions:
    1. Give a clear and simple answer.
    2. Do not use information outside the context.
    3. If the answer is not available, say so.
    4. Mention the PDF filename and page number
       for the information used.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = llm.invoke(prompt)

    return response.content
