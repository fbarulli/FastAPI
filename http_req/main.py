from logger import logger


from fastapi import FastAPI


api = FastAPI()


@api.get('/')
@logger.log_function
def get_index():
    data={'data': 'hello world'}               #extra: expects a dict    
    return data
