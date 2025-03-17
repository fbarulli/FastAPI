import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from fastapi import FastAPI
from http_req.logger import logger  
from data import Question, data
app = FastAPI()



# /question?use=exam&subject=math
@app.get("/questions")
async def get_all_questions(use: str = None):
    return {"questions" : }