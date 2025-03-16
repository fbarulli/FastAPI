import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from fastapi import FastAPI
from http_req.logger import logger  
from data import Question, data
app = FastAPI()

# the user must be able to choose a test type (use) 


@app.get("/questions/use/{question_id}/")
@logger.log_function
def get__by_id(question_id: int) -> Optional[Union[question, str]]:
    result = [question for question in questions_db if question.question_id == question_id]
    return result[0] if result else ""


# as well as one or more categories (subject).