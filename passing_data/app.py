# passing_data/app.py
from fastapi import FastAPI
from typing import Optional
from data import User, users_db  # Import from local data.py
from http_req.logger import logger  # Import logger from http_req

app = FastAPI()

@app.get("/user/{user_id}/")
@logger.log_function
def get_user_by_id(user_id: int) -> Optional[User]:
    result = [user for user in users_db if user.user_id == user_id]
    return result[0] if result else None

@app.get("/")
@logger.log_function
def get_index():
    return "Hey loser"