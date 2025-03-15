from logger import logger
from fastapi import FastAPI
import traceback

api = FastAPI()


@api.get('/')
def get_index():
    logger.logger.info("get_index() has started")
    try:
    except Exception as e:    
    
    return {'data': 'hello world'}