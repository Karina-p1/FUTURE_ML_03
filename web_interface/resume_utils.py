import re, joblib
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
import nltk
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

vectorizer = joblib.load("../models/resume_vectorizer.pkl")

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w not in stop_words]
    return " ".join(tokens)

def process_ranking(df, job_description, skills_list):
    df = df[['Resume_str']].dropna().reset_index(drop=True)
    df['resume_id'] = df.index
    df['clean_resume'] = df['Resume_str'].apply(clean_text)
    
    clean_job = clean_text(job_description)
    resume_vectors = vectorizer.transform(df['clean_resume'])
    job_vector = vectorizer.transform([clean_job])

    df['match_score'] = cosine_similarity(resume_vectors, job_vector).flatten()
    
    def extract_skills(text):
        return [s for s in skills_list if s in text]

    df['matched_skills'] = df['clean_resume'].apply(extract_skills)
    df['missing_skills'] = df['matched_skills'].apply(lambda x: list(set(skills_list)-set(x)))
    df['skill_score'] = df['matched_skills'].apply(lambda x: len(x)/len(skills_list) if skills_list else 0)
    
    df['final_score'] = (0.7*df['match_score'] + 0.3*df['skill_score'])
    df = df.sort_values(by='final_score', ascending=False).reset_index(drop=True)
    df['rank'] = df.index + 1
    
    return df[['rank','resume_id','final_score','matched_skills','missing_skills']].head(10).to_dict(orient='records')