from logger import logger


from fastapi import FastAPI


api = FastAPI()


@api.get('/')
@logger.log_function
def get_index():
    data={'data': 'hello world'}               #extra: expects a dict    
    return data

@api.get('/other')
@logger.log_function
def get_other():
    return {
        'method': 'get',
        'endpoint': '/other'
    }
@api.post('/')
@logger.log_function
def post_index():
    return {
        'method': 'post',
        'endpoint': '/'
        }
@api.delete('/')
@logger.log_function
def delete_index():
    return {
        'method': 'delete',
        'endpoint': '/'
        }
@api.put('/')
@logger.log_function
def put_index():
    return {
        'method': 'put',
        'endpoint': '/'
        }
@api.patch('/')
@logger.log_function
def patch_index():
    return {
        'method': 'patch',
        'endpoint': '/'
        }
