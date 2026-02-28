# Internship: Future Interns – Machine Learning
**CIN ID:** FIT/JAN26/ML5215  
**Task:** Resume Screening System (Task 3)

# 📄 AI Resume Ranker – FastAPI + NLP Based Candidate Ranking System

## 🚀 Overview
This project is an AI-powered Resume Screening & Candidate Ranking System designed to evaluate resumes against a job description using semantic similarity and skill-based scoring.  
The system combines NLP preprocessing, TF-IDF vectorization, cosine similarity, and FastAPI deployment to deliver real-time ranking results via a modern web interface.

## 🎯 Problem Statement
Manual resume screening:
- Is time-consuming
- Lacks consistency
- Does not scale efficiently

This system automates:
- Resume-job semantic matching
- Skill gap analysis
- Candidate ranking
- Top candidate extraction

## 🧠 Core ML Logic
The ranking system uses a hybrid scoring approach:  
**Final Score = 70% Semantic Similarity (TF-IDF + Cosine Similarity) + 30% Skill Match Score**

**NLP Pipeline:**
- Lowercase normalization
- Regex cleaning
- Tokenization (NLTK)
- Stopword removal
- TF-IDF vectorization
- Cosine similarity calculation

## 🛠 Tech Stack
- Python  
- Pandas  
- NLTK  
- Scikit-learn  
- TF-IDF Vectorization  
- Cosine Similarity  
- FastAPI  
- HTML + JavaScript

## 📂 Project Structure

| Folder / File | Description |
|---------------|-------------|
| `models/resume_vectorizer.pkl` | Pre-trained TF-IDF vectorizer for semantic similarity |
| `notebook/resume_screening.ipynb` | Jupyter Notebook with ML preprocessing, ranking pipeline, and evaluation |
| `exports/enhanced_resume_ranking.csv` | Output CSV with ranked resumes and scores |
| `exports/top_candidates.csv` | Top 10 ranked candidate resumes |
| `plots/resume_category_distribution.png` | Visualization of resume categories |
| `plots/resume_length_distribution.png` | Resume length distribution |
| `plots/top_common_words.png` | Most common words across resumes |
| `web_interface/app.py` | FastAPI backend application |
| `web_interface/resume_utils.py` | Helper functions for text preprocessing and scoring |
| `web_interface/templates/index.html` | Frontend HTML interface |
| `requirements.txt` | Python dependencies |

## 🌐 Web Interface Features
- Upload Resume CSV  
- Enter Job Description  
- Provide Required Skills  
- Demo Mode  
- Real-time Ranking Results  
- Matched & Missing Skill Highlighting  
- Loading Animation  
- Clean Dark UI Design

## 📊 Output Format
Returns top 10 ranked candidates with:  
- Rank  
- Resume ID  
- Final Score  
- Matched Skills  
- Missing Skills

## ⚙️ Installation
```bash
git clone https://github.com/karina-p1/FUTURE_ML_03.git
cd FUTURE_ML_03
pip install -r requirements.txt
uvicorn web_interface.app:app --reload
# Open in browser: http://127.0.0.1:8000

### 👩‍💻 Author
Karina Paudel
