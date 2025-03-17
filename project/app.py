# app.py
import sys
import os
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



print("sys.path:", sys.path)  # Debug line
print("Current dir:", os.getcwd())  # Debug line








from fastapi import FastAPI, HTTPException
from project.logger.logger import TextLogger as logger
from project.data.data import Question, questions
from typing import List, Dict, Any










app = FastAPI()








# /questions
@app.get("/questions")
@logger.log_function
async def get_all_questions() -> Dict[str, Any]:
    '''
    returns : dict with all questions
    '''
    try:
        return {"questions": questions}
    except Exception as e:
        error_msg = f"Failed {str(e)}"
        raise HTTPException(status_code=500, detail=error_msg)