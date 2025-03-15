from logger import logger


from fastapi import FastAPI


api = FastAPI()


@api.get('/')
def get_index():
    logger.logger.info("get_index() has started", extra={"endpoint": "/", "method": "GET"})
    data={'data': 'hello world'}               #extra: expects a dict
    logger.logger.info("get_index() finished", extra={"endpoint": "/", "method": "GET"})
    return data
