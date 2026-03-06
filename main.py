import streamlit as st
from rag import *

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Bhagavad Gita AI Guide",
    page_icon="🕉️",
    layout="wide"
)

# ---------------- Load RAG Pipeline ----------------
@st.cache_resource
def load_rag_pipeline():

    documents = load_documents()
    chunks = split_documents(documents)
    embeddings = create_embeddings()
    vectorstore = create_vector_db(chunks, embeddings)

    return vectorstore


vectorstore = load_rag_pipeline()


# ---------------- Custom Styling ----------------
st.markdown("""
<style>

.title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: #e67e22;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: gray;
    margin-bottom: 40px;
}

.response-box {
    background-color: #fff5e6;
    padding: 30px;
    border-radius: 15px;
    margin-top: 25px;
    font-size: 18px;
}

.stButton button {
    background-color: #e67e22;
    color: white;
    font-size: 18px;
    border-radius: 8px;
    height: 50px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.markdown(
    '<div class="title">🕉️ Bhagavad Gita AI Guide</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask any life question and receive wisdom from the Bhagavad Gita</div>',
    unsafe_allow_html=True
)

# ---------------- Layout ----------------
col1, col2 = st.columns([2,1])

with col1:

    user_question = st.text_area(
        "Ask your life question",
        height=200,
        placeholder="Example: How should I deal with stress or confusion in life?"
    )

    if st.button("Get Wisdom ✨", use_container_width=True):

        if user_question.strip() == "":
            st.warning("Please enter your question")

        else:

            with st.spinner("Searching Bhagavad Gita wisdom..."):

                # -------- RAG Pipeline --------
                context = retrieve_context(vectorstore, user_question)

                answer = generate_answer(user_question, context)

            st.markdown(
                f'<div class="response-box">{answer}</div>',
                unsafe_allow_html=True
            )

# ---------------- Side Panel ----------------
with col2:

    st.info("""
### 🧘 How Bhagavad Gita Helps

The Bhagavad Gita provides wisdom for:

• Stress and anxiety  
• Confusion in life  
• Fear and failure  
• Duty and responsibility  
• Finding inner peace
""")

    st.success("📖 Source: Bhagavad Gita Teachings")

# ---------------- Footer ----------------
st.markdown("---")
st.caption("🕉️ Bhagavad Gita AI Guide • Spiritual Wisdom Assistant")