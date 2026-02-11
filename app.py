# !pip install streamlit PyPDF2 sentence-transformers

import streamlit as st
from sentence_transformers import SentenceTransformer, util
from PyPDF2 import PdfReader
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.title("📄 ATS Resume Checker")
st.write("Upload your resume and compare it with a Job Description using NLP.")

# Read resume PDF from upload
def read_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
           text += page.extract_text()
    return text


uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")
job_description = st.text_area("Paste Job Description")


# Run ATS only when both inputs are present
if uploaded_file is not None and job_description.strip() != "":

    resume_text = read_pdf(uploaded_file)

    model = SentenceTransformer("all-MiniLM-L6-v2")

    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    jd_embedding = model.encode(job_description, convert_to_tensor=True)

    similarity_score = util.cos_sim(resume_embedding, jd_embedding)
    ats_score = round(float(similarity_score[0][0]) * 100, 2)

    st.subheader("📊 ATS Match Result")
    st.progress(int(ats_score))
    st.write(f"### ATS Match Score: **{ats_score}%**")

    if ats_score >= 75:
        st.success("🎉 Excellent match! Your resume is ATS-friendly.")
    elif ats_score >= 50:
        st.warning("⚠️ Moderate match. Improve keywords.")
    else:
        st.error("❌ Low match. Resume needs optimization.")

else:
    st.info("👆 Please upload a resume and paste the Job Description.")
