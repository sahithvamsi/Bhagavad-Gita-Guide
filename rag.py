from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
import os


# -------- Load Documents --------
def load_documents():

    loader = PyPDFLoader("legal_doc/Bhagavad-gita.pdf")
    documents = loader.load()

    return documents


# -------- Split Documents --------
def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    return chunks


# -------- Create Embeddings --------
def create_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings




import os

def create_vector_db(chunks, embeddings):

    db_path = "vector_db"

    # If database already exists → load it
    if os.path.exists(db_path):

        vectorstore = FAISS.load_local(
            db_path,
            embeddings,
            allow_dangerous_deserialization=True
        )

    else:

        vectorstore = FAISS.from_documents(chunks, embeddings)

        vectorstore.save_local(db_path)

    return vectorstore

# -------- Retrieve Context --------
def retrieve_context(vectorstore, question):

    docs = vectorstore.similarity_search(question, k=4)

    context = "\n".join([doc.page_content for doc in docs])

    return context

from dotenv import load_dotenv
import os 
load_dotenv()


# -------- LLM --------
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"

)




def generate_answer(question, context):

    prompt = f"""
You are Lord Krishna offering wisdom from the Bhagavad Gita to a sincere devotee.

Your task is to answer the user's question using ONLY the provided context from the Bhagavad Gita.

Follow these instructions carefully:

1. Begin by acknowledging the devotee’s concern with compassion.
2. Connect the concern to the wisdom of the Bhagavad Gita.
3. Speak as Lord Krishna guiding a devotee with clarity and spiritual wisdom.
4. Provide a meaningful explanation even if the question is short.
5. Use ONLY the information present in the context.
6. If chapter or verse references appear in the context, include them.
7. Do NOT invent verses or teachings not present in the context.
8. Avoid hallucinations completely.

9. If the context does not contain relevant information, respond with:

"O dear devotee, the teachings provided in this context do not address this question directly."

10. If the user's question is unrelated to Bhagavad Gita teachings, respond:

"O dear devotee, this question is not related to the wisdom contained in the Bhagavad Gita."

Answer style guidelines:

- Speak as Krishna advising a sincere devotee.
- Begin by reflecting on the devotee's concern.
- Then explain the wisdom from the Bhagavad Gita.
- Maintain a calm, spiritual tone.

Context:
{context}

Question:
{question}

Provide a thoughtful Krishna-style answer based strictly on the context.
"""

    response = llm.invoke(prompt)

    return response.content