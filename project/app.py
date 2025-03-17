import sys 
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
print("sys.path:", sys.path)   
print("Current dir:", os.getcwd())   

from fastapi import FastAPI, HTTPException, Request
from project.data.data import Question, questions
from typing import Dict, Any, List

app = FastAPI()  

#!curl -X GET "http://127.0.0.1:8000/questions"
@app.get("/questions") 
async def get_all_questions():     
    '''     
    returns : dict with all questions     
    '''
    try:
        return {"questions": [q.model_dump() for q in questions]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get questions: {str(e)}")

@app.get("/questions/use") 
async def get_all_uses():     
    '''     
    returns : dict with all uses     
    '''
    try:
        unique_uses = list(set(q.use for q in questions))
        return {"uses": unique_uses}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get uses: {str(e)}")


# !curl -X GET "http://127.0.0.1:8000/questions/use"
@app.get('/questions/{use}') 
async def get_questions_by_use(use: str):     
    '''     
    returns : dict filtered by use     
    '''
    try:
        questions_by_use = [q.model_dump() for q in questions if q.use == use]
        return {"questions_by_use": questions_by_use}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get questions by use: {str(e)}")