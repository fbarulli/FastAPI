from http_req.logger import logger
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


users_db = [
    {
        'user_id': 1,
        'name': 'Alice',
        'subscription': 'free tier'
    },
    {
        'user_id': 2,
        'name': 'Bob',
        'subscription': 'premium tier'
    },
    {
        'user_id': 3,
        'name': 'Clementine',
        'subscription': 'free tier'
    }
]

class User(BaseModel):
    user_id: int
    name: str
    subscription: str

users_db = [User(**user) for user in users_db]


@app.get('/user/{user_id}')
@logger.log_function
def get_user_by_id(user_id: int) -> Optional[User]:
    result = [user for user in users_db if user.user_id == user_id]
    return result[0] if result else None