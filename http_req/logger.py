import logging
import os
from typing import Optional


log_dir = "logs"
os.mkdir(log_dir, exist_ok=True)

class TextLogger:

    def __init__(self, filename: str = "app.log", log_dir: str = "logs") -> None:
        
        os.makedirs(log_dir, exist_ok=True) #create log_dir
        
        self.logger: logging.Logger = logging.getlogger("FastAPI") #create logger
        self.logger.setLevel(logging.INFO)
        
        log_path : str = os.path.join(log_dir, filename)
        formatter : logging.Formatter = logging.FileHandler(log_)
        
        