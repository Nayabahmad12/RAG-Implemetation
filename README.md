\# 📚 PDF RAG Chatbot



A PDF-based AI chatbot that allows users to upload PDF documents and ask questions about their content. It uses \*\*Retrieval-Augmented Generation (RAG)\*\* to retrieve relevant information from PDFs and generate answers using a Large Language Model (LLM).



\## 🚀 Features



\- Upload and process PDF documents.

\- Extract text from PDF files.

\- Split documents into smaller text chunks.

\- Generate embeddings using Hugging Face.

\- Store document embeddings in ChromaDB.

\- Retrieve relevant information using semantic similarity search.

\- Generate answers using Groq LLM.

\- Interactive chatbot interface using Streamlit.

\- Display retrieved PDF sources and page numbers.



\## 🛠️ Technologies Used



| Technology | Purpose |

|---|---|

| Python | Programming language |

| LangChain | RAG application framework |

| PyPDF | PDF text extraction |

| Hugging Face | Text embeddings |

| ChromaDB | Vector database |

| Groq API | LLM-based answer generation |

| Streamlit | Web interface |



\## 📂 Project Structure



```text

PDF-RAG-Chatbot/

│

├── src/

│   ├── answer\_generator.py

│   ├── document\_loader.py

│   ├── llm.py

│   ├── retriever.py

│   ├── text\_splitter.py

│   └── vector\_store.py

│

├── data/

│   └── pdf/

│

├── app.py

├── streamlit\_app.py

├── requirements.txt

├── .gitignore

└── README.md

```



\## ⚙️ Installation and Setup



\### 1. Clone the repository



```bash

git clone https://github.com/Nayabahmad12/PDF-RAG-Chatbot.git

```



\### 2. Open the project folder



```bash

cd PDF-RAG-Chatbot

```



\### 3. Create a virtual environment



```bash

python -m venv venv

```



\### 4. Activate the virtual environment



For Windows:



```bash

venv\\Scripts\\activate

```



\### 5. Install dependencies



```bash

pip install -r requirements.txt

```



\### 6. Configure Groq API key



Create a `.env` file in the project root:



```env

GROQ\_API\_KEY=your\_groq\_api\_key

```



Get your API key from \[Groq Console](https://console.groq.com/keys).



\*\*Important:\*\* Never upload your `.env` file or API key to GitHub.



\## ▶️ Run the Project



\### Streamlit Web Application



```bash

streamlit run streamlit\_app.py

```



Open the local URL displayed in your terminal, usually:



```text

http://localhost:8501

```



\### Terminal-based Chatbot



```bash

python app.py

```



\## 🔄 How It Works



1\. \*\*Document Loading:\*\* Extracts text from uploaded PDF files.

2\. \*\*Text Splitting:\*\* Divides extracted text into smaller chunks.

3\. \*\*Embedding Generation:\*\* Converts text chunks into numerical vectors using Hugging Face embeddings.

4\. \*\*Vector Storage:\*\* Stores embeddings in ChromaDB.

5\. \*\*Retrieval:\*\* Finds the most relevant chunks based on the user's question.

6\. \*\*Answer Generation:\*\* Sends retrieved context to the Groq LLM to generate an answer.



\## 🧠 RAG Architecture



&#x20; text

&#x20;       PDF Documents

&#x20;             |

&#x20;             v

&#x20;      Document Loading

&#x20;             |

&#x20;             v

&#x20;        Text Splitting

&#x20;             |

&#x20;             v

&#x20;     Embedding Generation

&#x20;             |

&#x20;             v

&#x20;         ChromaDB

&#x20;             |

&#x20;             v

&#x20;       User Question

&#x20;             |

&#x20;             v

&#x20;      Similarity Search

&#x20;             |

&#x20;             v

&#x20;     Relevant Documents

&#x20;             |

&#x20;             v

&#x20;         Groq LLM

&#x20;             |

&#x20;             v

&#x20;      Generated Answer



