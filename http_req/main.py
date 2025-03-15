import os
from fastapi import FastAPI
import traceback

api = FastAPI()


@api.get('/')
def get_index():
    return {'data': 'hello world'}