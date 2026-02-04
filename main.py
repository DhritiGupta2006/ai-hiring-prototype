from fastapi import FastAPI, UploadFile
from resume_parser import parse_resume
from scoring import score_resume
from report import generate_report

app = FastAPI()

RUBRIC = {"python": 5, "fastapi": 3, "postgresql": 4}

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile):
    text = (await file.read()).decode("utf-8")
    keywords = parse_resume(text)
    scoring_result = score_resume(keywords, RUBRIC)
    explanation = generate_report(scoring_result)
    return {
        "keywords": keywords,
        "score": scoring_result["total_score"],
        "report": explanation
    }
