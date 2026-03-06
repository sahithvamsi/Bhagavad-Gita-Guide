                                       🕉️ Bhagavad Gita AI Guide

Bhagavad Gita AI Guide is an AI-powered spiritual guidance application that provides answers to life questions using the wisdom of the Bhagavad Gita.

The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant verses from the Bhagavad Gita and generate responses in the style of Lord Krishna guiding a sincere devotee, similar to how Krishna advised Arjuna.

🌐 Live Application:
https://bhagavad-gita-guide-ezr8gvsvtay3ntypbnm9ng.streamlit.app/

✨ Features
✅ Ask life-related questions
✅ Retrieves relevant teachings from the Bhagavad Gita
✅ AI generates answers in Krishna-style wisdom
✅ Uses RAG architecture to avoid hallucinations
✅ Clean Streamlit user interface
✅ Embeddings powered by Sentence Transformers
✅ Fast LLM responses using Groq LLaMA models

🧠 How It Works
The application follows a Retrieval-Augmented Generation (RAG) pipeline.

1️⃣ Document Loading
The Bhagavad Gita PDF is loaded using:

PyPDFLoader
2️⃣ Document Splitting
The text is split into smaller chunks using:

RecursiveCharacterTextSplitter
This improves search accuracy.

3️⃣ Embeddings
Each chunk is converted into vector embeddings using:

sentence-transformers/all-MiniLM-L6-v2
4️⃣ Vector Database
The embeddings are stored in a FAISS vector database for fast semantic search.

5️⃣ Retrieval
When a user asks a question:

The system finds the most relevant Bhagavad Gita passages

These passages are used as context

6️⃣ Response Generation
The retrieved context is sent to the Groq LLaMA model, which generates an answer in the voice of Lord Krishna.

🏗 Project Structure
Bhagavad-Gita-AI-Guide
│
├── main.py                # Streamlit app
├── rag.py                 # RAG pipeline
├── requirements.txt       # Dependencies
├── .env                   # API key (not uploaded)
├── vector_db/             # FAISS database
│
├── legal_doc/
│   └── Bhagavad-gita.pdf  # Source text
│
└── README.md
⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/bhagavad-gita-ai-guide.git
cd bhagavad-gita-ai-guide
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Create .env file
GROQ_API_KEY=your_api_key_here
⚠️ Do not upload .env to GitHub.

4️⃣ Run the application
streamlit run main.py
📦 Requirements
streamlit
langchain
langchain-community
langchain-text-splitters
langchain-groq
faiss-cpu
sentence-transformers
huggingface-hub
pypdf
python-dotenv





💡 Example Questions
You can ask questions like:

How should I deal with stress in life?

What does Bhagavad Gita say about duty?

How can I overcome fear?

What is the meaning of karma?

How should a person handle failure?

The AI will respond with Bhagavad Gita wisdom.
