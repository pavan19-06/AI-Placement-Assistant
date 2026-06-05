import streamlit as st
from src.chatbot import ask_question
from pypdf import PdfReader

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Placement Assistant",
    page_icon="🚀",
    layout="wide"
)

# ---------------- SESSION STATE ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- RESUME FUNCTIONS ----------------

def extract_resume_text(uploaded_file):
    text = ""

    try:
        pdf = PdfReader(uploaded_file)

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except:
        pass

    return text

def simple_resume_analysis(text):

    score = 60

    keywords = [
        "python",
        "java",
        "sql",
        "machine learning",
        "project",
        "internship",
        "github",
        "skills",
        "education"
    ]

    found = []

    for word in keywords:
        if word.lower() in text.lower():
            found.append(word)
            score += 4

    score = min(score, 100)

    return score, found

# ---------------- CSS ----------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
font-family:'Poppins',sans-serif;
}

.stApp{
background:
linear-gradient(
135deg,
#050816,
#0A1025,
#111827,
#1E1B4B
);
color:white;
}

section[data-testid="stSidebar"]{
background:rgba(255,255,255,0.04);
backdrop-filter:blur(30px);
border-right:1px solid rgba(255,255,255,0.08);
}

.glass{
background:rgba(255,255,255,0.05);
backdrop-filter:blur(30px);
border:1px solid rgba(255,255,255,0.1);

box-shadow:
0 8px 32px rgba(0,0,0,0.3),
0 0 25px rgba(59,130,246,0.1);

border-radius:25px;
padding:25px;
margin-bottom:20px;
}

.hero{
text-align:center;
padding-top:20px;
padding-bottom:20px;
}

.hero h1{
font-size:80px;
font-weight:800;

background:linear-gradient(
90deg,
#ffffff,
#6ee7ff,
#60a5fa,
#8b5cf6
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.hero p{
font-size:22px;
color:#d1d5db;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("## 📚 Subjects")

    st.markdown("""
    • DBMS

    • DSA

    • OOP

    • Resume

    • Aptitude

    • Interview Prep
    """)

    st.success("RAG Active ✅")

    st.divider()

    st.markdown("## 📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    if uploaded_file:
        st.success("Resume Uploaded ✅")

    analyze_btn = st.button("🚀 Analyze Resume")

    st.divider()

    st.markdown("## 👨‍💻 Developer")

    st.write("Pavan R")
    st.write("AI & ML Student")
    st.write("Gemini + LangChain + FAISS")

    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------- HERO ----------------

st.markdown("""
<div class="hero">
<h1>AI Placement Assistant 🚀</h1>
<p>Learn Faster • Prepare Better • Get Placed</p>
</div>
""", unsafe_allow_html=True)

# ---------------- STATS ----------------

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="glass">
    <h2>🤖 Gemini</h2>
    <p>AI Model</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="glass">
    <h2>📦 FAISS</h2>
    <p>Vector Database</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="glass">
    <h2>🧠 RAG</h2>
    <p>Mode</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- RESUME ANALYSIS ----------------

if uploaded_file and analyze_btn:

    resume_text = extract_resume_text(uploaded_file)

    score, found = simple_resume_analysis(resume_text)

    st.markdown("## 📄 Resume Analysis")

    col1, col2 = st.columns([1,2])

    with col1:
        st.metric("ATS Score", f"{score}/100")

    with col2:
        st.success("Resume successfully analyzed")

    st.markdown("### ✅ Keywords Found")

    if found:
        st.write(", ".join(found))
    else:
        st.warning("No major keywords detected")

    st.markdown("### 💡 Suggestions")

    st.markdown("""
    - Add measurable achievements
    - Add GitHub links
    - Add project descriptions
    - Include internships
    - Add technical skills section
    - Use ATS-friendly formatting
    """)

# ---------------- CHAT HISTORY ----------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------- CHAT INPUT ----------------

question = st.chat_input(
    "Ask anything about DBMS, DSA, Resume, OOP..."
)

if question:

    st.session_state.messages.append({
        "role":"user",
        "content":question
    })

    with st.chat_message("user"):
        st.write(question)

    with st.spinner("Thinking..."):

        try:
            answer = ask_question(question)

        except Exception as e:
            answer = str(e)

    st.session_state.messages.append({
        "role":"assistant",
        "content":answer
    })

    with st.chat_message("assistant"):
        st.write(answer)