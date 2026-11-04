
def retrieve_documents(vector_store, question):

    results = vector_store.similarity_search(
        query=question,
        k=3
    )

    return results
