ATS-Resume-Checker
An AI-powered tool that compares resumes with job descriptions using sentence embeddings to generate an ATS-style match score.

✨ Project Overview
Recruiters use Applicant Tracking Systems (ATS) to filter resumes before human review.
This project simulates an ATS by intelligently comparing resume content with job requirements and providing a clear match score.

🚀 Key Features
  📤 Upload resume in PDF format
  📝 Paste job description
  🤖 AI-based semantic similarity matching
  📊 ATS match score with status:
    🎯 Strong Match
    ⚠️ Moderate Match
    ❌ Weak Match

 🧠 How It Works
  1.) Resume text is extracted from the uploaded PDF.
  2.) Resume and job description are converted into vector embeddings using a pre-trained Sentence Transformer model.
  3.) Cosine similarity is calculated between the two embeddings.
  4.) The similarity score is converted into a percentage and displayed as an ATS match result.

Technologies Used
1. Python
2. Streamlit (Web UI)
3. Sentence Transformers (all-MiniLM-L6-v2)
4. PyPDF
5. PyTorch
6. Cosine Similarity

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
   
