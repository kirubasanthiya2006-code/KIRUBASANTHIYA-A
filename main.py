from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import shutil
import os

app = FastAPI(title="InternReview AI API", version="1.0.0")

class Intern(BaseModel):
    intern_id: str
    name: str
    email: str
    project_title: str
    review_date: str
    review_time: str
    project_link: str
    status: str = "Pending"

@app.get("/")
def read_root():
    return {"message": "Welcome to InternReview AI API"}

@app.post("/api/upload-excel/")
async def upload_excel(file: UploadFile = File(...)):
    if not file.filename.endswith(('.xlsx', '.csv')):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload Excel or CSV.")
    return {"filename": file.filename, "status": "Successfully parsed and validated."}

@app.post("/api/submit-project/")
async def submit_project(intern_id: str, repo_link: str):
    return {"intern_id": intern_id, "repo_link": repo_link, "status": "Under AI Review"}
