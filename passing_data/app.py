# passing_data/app.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from data import User, users_db  
from http_req.logger import logger  
from typing import Optional, Union


app = FastAPI()

@app.get("/user/{user_id}/")
@logger.log_function
def get_user_by_id(user_id: int) -> Optional[Union[User, str]]:
    result = [user for user in users_db if user.user_id == user_id]
    return result[0] if result else ""

@app.get("/")
@logger.log_function
def get_user():
    return "Hey loser"

@app.get("/users")
@logger.log_function
def get_users():
    return users_db

@app.get("/users/{name}")
@logger.log_function
def get_user_by_name(name: str) -> Optional[Union[User, str]]:
    result = [user for user in users_db if user.name == name]
    return result[0] if result else ""

@app.get("/user/{user_id}/subscription")
@logger.log_function
def get_sub_by_name(user_id: int) -> Optional[Union[User, str]]:
    result = [user for user in users_db if user.user_id == user_id]
    return result[0].subscription if result else ""


#  Request string
from typing import Optional
@app.get('/addition')
@logger.log_function
def get_addition(a: int, b: Optional[int]=None):
    if b:
        result = a + b
    else:
        result = a + 1
    return {
        'addition_result': result
    }
    
#  Headers
from fastapi import Header

@app.get('/headers')
# pylint: disable=dangerous-default-value
# pyright: ignore
async def get_headers(user_agent: str | None = Header(None)):  # type: ignore
    return {
        'User-Agent': user_agent
    }