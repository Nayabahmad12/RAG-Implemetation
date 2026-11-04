import os
from langchain_community.document_loaders import PyPDFLoader

def load_documents():

    folder_path = "data/pdf"
    all_documents = []

    for filename in os.listdir(folder_path):

        if filename.endswith(".pdf"):

            file_path = os.path.join(folder_path, filename)

            loader = PyPDFLoader(file_path)

            documents = loader.load()

            all_documents.extend(documents)

    return all_documents