from http_req.logger import logger
from fastapi import FastAPI
from typing import Optional, TypedDict

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






class User(TypeDict):
    user_id :int
    name : str
    subscription :str




@api.get('/user/{user_id:int}/')
@logger.log_function
def get_user_by_id(user_id: int) -> Optional[User]:
    result = [user for user in users_db if user['user_id'] == user_id]
    return result[0] if result else None  