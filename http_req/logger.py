# logger.py


import logging
import os
from functools import wraps


log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

class TextLogger:

    def __init__(self, filename: str = "app.log", log_dir: str = "logs", level: int = logging.DEBUG) -> None:
        
        os.makedirs(log_dir, exist_ok=True) #create log_dir
        self.logger: logging.Logger = logging.getLogger("FastAPI") #create logger
        
        self.logger.setLevel(level) 
        
        log_path : str = os.path.join(log_dir, filename)
        handler = logging.FileHandler(log_path)
        formatter = logging.Formatter(fmt = "%(asctime)s - %(levelname)s - %(message)s  - %(endpoint)s  - %(method)s ")
        
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
    def log_function(self,func):
        @wraps(func)                        #preservers original func metadata
        self.logger.info(f"{func.__name__} was called", extra)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
logger : TextLogger = TextLogger()
