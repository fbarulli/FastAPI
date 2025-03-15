from pydantic import BaseModel
class User(BaseModel):
    user_id: int
    name: str
    subscription: str
user_data = [
    {'user_id': 1, 'name': 'Alice', 'subscription': 'free tier'},
    {'user_id': 2, 'name': 'Bob', 'subscription': 'premium tier'},
    {'user_id': 3, 'name': 'Clementine', 'subscription': 'free tier'}
]
users_db = [User(**user) for user in user_data]