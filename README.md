ATS Resume Checker (NLP-Based)

✨ Project Overview
An AI-powered ATS (Applicant Tracking System) Resume Checker built using **Python, NLP, and Streamlit**.  
This application compares a candidate's resume with a job description and calculates a semantic similarity score using Sentence Transformers.

🚀 Key Features
  📤 Upload resume in PDF format
  📝 Paste job description
  🤖 AI-based semantic similarity matching
  📊 ATS match score with status:
    🎯 Strong Match
    ⚠️ Moderate Match
    ❌ Weak Match

🧠 How It Works

1. Resume PDF is uploaded.
2. Text is extracted using PyPDF2.
3. Job Description is taken as input.
4. Both texts are converted into embeddings using `all-MiniLM-L6-v2`.
5. Cosine similarity is calculated using tensor operations.
6. Final ATS match score is displayed.

🛠️ Tech Stack

- Python
- Streamlit
- Sentence Transformers (MiniLM Model)
- PyPDF2
- PyTorch
- NumPy

▶️ How to Run the Project
Step 1: Clone the Repository
git clone https://github.com/your-username/ATS_Resume_Checker.git
cd ATS_Resume_Checker

pip install -r requirements.txt

streamlit run app.py
The application will open automatically in your browser.

📊 Sample Output

Resume Match Score: 78% Status: 🎯 Strong Match

🌟 Future Enhancements

Keyword gap analysis
Skill-wise matching
Resume improvement suggestions
Downloadable ATS report
Multiple resume comparison
   
