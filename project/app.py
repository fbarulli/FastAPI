# app.py
from fastapi import FastAPI, HTTPException
from project.data.data import questions, Question
from typing import List, Dict, Any, Optional, cast
from pandas import DataFrame

app = FastAPI()

@app.get("/questions", response_model=Dict[str, List[Dict[str, Any]]])
async def get_all_questions() -> Dict[str, List[Dict[str, Any]]]:
    """
    curl -X GET "http://127.0.0.1:8000/questions"
    """
    try:
        df = Question.to_dataframe(questions)
        records = cast(List[Dict[str, Any]], df.to_dict(orient="records"))
        return {"questions": records}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get questions: {str(e)}")

@app.get("/questions/use", response_model=Dict[str, List[str]])
async def get_all_uses() -> Dict[str, List[str]]:
    """
    curl -X GET "http://127.0.0.1:8000/questions/use"
    """
    try:
        df = Question.to_dataframe(questions)
        unique_uses = list(df['use'].unique().tolist())
        return {"uses": unique_uses}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get uses: {str(e)}")

@app.get("/questions/subject", response_model=Dict[str, List[str]])
async def get_all_subjects() -> Dict[str, List[str]]:
    """
    curl -X GET "http://127.0.0.1:8000/questions/subject"
    """
    try:
        df = Question.to_dataframe(questions)
        unique_subjects = list(df['subject'].unique().tolist())
        return {"subject": unique_subjects}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get subjects: {str(e)}")

@app.get('/questions/filter', response_model=Dict[str, List[Dict[str, Any]]])
async def filter_questions(subjects: Optional[List[str]] = None) -> Dict[str, List[Dict[str, Any]]]:
    """
    curl -X GET "http://127.0.0.1:8000/questions/filter?subjects=Math&subjects=Science"
    """
    try:
        df = Question.to_dataframe(questions)
        if subjects:
            df = df[df['subject'].isin(subjects)]
        records = cast(List[Dict[str, Any]], df.to_dict(orient="records"))
        return {"filtered_questions": records}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to filter questions: {str(e)}")

@app.get('/questions/{use}', response_model=Dict[str, List[Dict[str, Any]]])
async def get_questions_by_use(use: str) -> Dict[str, List[Dict[str, Any]]]:
    """
    curl -X GET "http://127.0.0.1:8000/questions/{use}"
    Example: curl -X GET "http://127.0.0.1:8000/questions/Validation%20test"
    """
    try:
        df = Question.to_dataframe(questions)
        filtered_df = df[df['use'] == use]
        records = cast(List[Dict[str, Any]], filtered_df.to_dict(orient="records"))
        return {"questions_by_use": records}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get questions by use: {str(e)}")