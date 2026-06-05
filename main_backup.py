import streamlit as st
from src.chatbot import ask_question

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Placement Assistant",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family: 'Inter', sans-serif;
}

/* Main Background */

.stApp{
background:
linear-gradient(
135deg,
#050816,
#0A1025,
#111827,
#1E1B4B
);
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background: rgba(255,255,255,0.03);
    backdrop-filter: blur(40px);
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Glass Cards */

.glass{
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(20px);
    border-radius: 20px;
    padding: 25px;
}

/* Hero Title */

.hero{
    text-align:center;
    padding-top:40px;
}

.hero h1{
    font-size:80px;
    font-weight:800;
    background: linear-gradient(
    90deg,
    #ffffff,
    #60a5fa,
    #a78bfa
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;

    text-shadow:
    0 0 20px rgba(96,165,250,0.4),
    0 0 40px rgba(168,85,247,0.3);
}

.hero p{
    color:#d1d5db;
    font-size:22px;
}

/* Chat Input */

input{
    border-radius:18px !important;
}

/* Buttons */

.stButton button{
    border-radius:15px;
    background:#2563eb;
    color:white;
    border:none;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("## 📚 Subjects")

    st.markdown("""
    - DBMS
    - DSA
    - OOP
    - Resume
    - Aptitude
    - Interview Prep
    """)

    st.success("RAG Active ✅")

    st.divider()

    st.markdown("### 👨‍💻 Developer")
    st.write("Pavan R")
    st.write("AI & ML Student")

# ---------------- HERO SECTION ----------------

st.markdown("""
<div class="hero">
<h1>AI Placement Assistant 🚀</h1>
<p>Learn Faster • Prepare Better • Get Placed</p>
</div>
""", unsafe_allow_html=True)

# ---------------- STATS ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="glass">
    <h3>🤖 Gemini</h3>
    <p>AI Model</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass">
    <h3>📦 FAISS</h3>
    <p>Vector Database</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="glass">
    <h3>🧠 RAG</h3>
    <p>Mode</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------- QUESTION BOX ----------------

question = st.text_input(
    "",
    placeholder="Ask anything about DBMS, DSA, Resume, OOP..."
)

# ---------------- RESPONSE ----------------

if question:

    with st.spinner("Thinking..."):

        answer = ask_question(question)

    st.markdown("### 💬 Answer")

    st.markdown(f"""
    <div class="glass">
    {answer}
    </div>
    """, unsafe_allow_html=True)