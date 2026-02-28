from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd
import io
from resume_utils import process_ranking

app = FastAPI(title="AI Resume Ranker")

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    with open("templates/index.html", encoding="utf-8") as f:
        return f.read()

@app.post("/rank")
async def rank_resumes(
    job_description: str = Form(...),
    skills: str = Form(...),
    file: UploadFile = File(None)   # optional now
):
    skills_list = [s.strip().lower() for s in skills.split(",") if s.strip()]

    # Demo mode: no file uploaded
    if file is None:
        df = pd.DataFrame({
            "Resume_str": [
                "Experienced Python and SQL data analyst with visualization skills",
                "Junior data scientist familiar with Python, Pandas and Machine Learning",
                "Python developer with NLP and data analysis experience"
            ]
        })
    else:
        content = await file.read()
        df = pd.read_csv(io.BytesIO(content))

    return process_ranking(df, job_description, skills_list)