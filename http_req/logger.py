# logger.py


import logging
import os



log_dir = "logs"
os.mkdir(log_dir, exist_ok=True)

class TextLogger:

    def __init__(self, filename: str = "app.log", log_dir: str = "logs") -> None:
        
        os.makedirs(log_dir, exist_ok=True) #create log_dir
        self.logger: logging.Logger = logging.getLogger("FastAPI") #create logger
        self.logger.setLevel(logging.DEBUG) 
        
        log_path : str = os.path.join(log_dir, filename)
        handler = logging.FileHandler(log_path)
        formatter = logging.Formatter(fmt = "%(asctime)s - %(levelname)s - %(messeage)s")
        
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
        
logger : TextLogger = TextLogger()
