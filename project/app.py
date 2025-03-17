# app.py
import sys 
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
print("sys.path:", sys.path)   
print("Current dir:", os.getcwd())   

from fastapi import FastAPI, HTTPException, Request
from project.logger.logger import TextLogger as logger
from project.data.data import Question, questions
from typing import Dict, Any, Callable, Coroutine  

app = FastAPI()  

def handle_errors(func: Callable[..., Coroutine[Any, Any, Dict[str, Any]]]) -> Callable[..., Coroutine[Any, Any, Dict[str, Any]]]:     
    """     
    A wrapper function to handle errors in FastAPI endpoints.     
    """     
    async def wrapper(*args, **kwargs) -> Dict[str, Any]:         
        try:             
            return await func(*args, **kwargs)         
        except Exception as e:             
            error_msg = f"Failed in {func.__name__}: {str(e)}"             
            raise HTTPException(status_code=500, detail=error_msg)          
    return wrapper   

#!curl -X GET "http://127.0.0.1:8000/questions" 
@app.get("/questions") 
@handle_errors 
async def get_all_questions(request: Request) -> Dict[str, Any]:     
    '''     
    returns : dict with all questions     
    '''     
    return {"questions": questions} 

#!curl -X GET "http://127.0.0.1:8000/questions/use" 
@app.get("/questions/use") 
@handle_errors 
async def get_all_uses(request: Request) -> Dict[str, Any]:     
    '''     
    returns : dict with all uses     
    '''     
    unique_uses = set(q.use for q in questions)     
    return {"uses": unique_uses}       

@app.get('/questions/{use}') 
@handle_errors 
async def get_questions_by_use(use: str, request: Request) -> Dict[str, Any]:     
    '''     
    returns : dict filtered by use     
    '''     
    questions_by_use = [q for q in questions if q.use == use]     
    return {"questions_by_use": questions_by_use}