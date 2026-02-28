# Internship: Future Interns – Machine Learning
**CIN ID:** FIT/JAN26/ML5215  
**Task:** Resume Screening System (Task 3)

## 🚀 AI Resume Ranker Overview
This project is an AI-powered Resume Screening & Candidate Ranking System designed to evaluate resumes against a job description using semantic similarity and skill-based scoring.  
The system combines NLP preprocessing, TF-IDF vectorization, cosine similarity, and FastAPI deployment to deliver real-time ranking results via a modern web interface.

### 🎯 Problem Statement
Manual resume screening:
- Is time-consuming
- Lacks consistency
- Does not scale efficiently

This system automates:
- Resume-job semantic matching
- Skill gap analysis
- Candidate ranking
- Top candidate extraction

### 🧠 Core ML Logic
Hybrid scoring: 70% Semantic Similarity + 30% Skill Match  
NLP Pipeline: Lowercase normalization, regex cleaning, tokenization (NLTK), stopword removal, TF-IDF vectorization, cosine similarity

### 🛠 Tech Stack
Python, Pandas, NLTK, Scikit-learn, TF-IDF, Cosine Similarity, FastAPI, HTML + JavaScript

### 📂 Project Structure
FUTURE_ML_03/
├── models/resume_vectorizer.pkl
├── notebook/resume_screening.ipynb
├── exports/enhanced_resume_ranking.csv
├── exports/top_candidates.csv
├── plots/...
├── web_interface/app.py
├── web_interface/resume_utils.py
├── web_interface/templates/index.html
└── requirements.txt

### 🌐 Web Interface Features
- Upload Resume CSV
- Enter Job Description
- Provide Required Skills
- Demo Mode
- Real-time Ranking
- Matched & Missing Skills
- Loading Animation
- Dark UI Design

### ⚙️ Installation
\`\`\`bash
git clone https://github.com/karina-p1/FUTURE_ML_03.git
cd FUTURE_ML_03
pip install -r requirements.txt
uvicorn web_interface.app:app --reload
# Open: http://127.0.0.1:8000
\`\`\`

### 🎫 Support Ticket Classification Overview
Machine Learning–based NLP system to classify and prioritize customer support tickets automatically.  

Tasks:
- Classify ticket category
- Assign priority (High/Medium/Low)
- Reduce response time & improve efficiency

### 🔄 ML Workflow
1️⃣ Data Cleaning  
2️⃣ Text Preprocessing (lowercase, punctuation removal, tokenization)  
3️⃣ Feature Engineering (TF-IDF)  
4️⃣ Model Training (Logistic Regression)  
5️⃣ Model Evaluation (Accuracy, Precision, Recall, F1, Confusion Matrix)  

### 🌐 Web Application Features
- Enter ticket text
- Predict category and priority
- Color-coded severity display
- Run locally: activate environment + uvicorn app.app:app --reload
- Open: http://127.0.0.1:8000

### 💡 Business Insights
- Automation Efficiency
- Faster Response Time
- Smart Resource Allocation
- Improved Customer Satisfaction

### 👩‍💻 Author
Karina Paudel
