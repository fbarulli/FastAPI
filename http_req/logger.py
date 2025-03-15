import logging
import os
from functools import wraps

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

class TextLogger:
    def __init__(self, filename: str = "app.log", log_dir: str = "logs", level: int = logging.DEBUG) -> None:
        os.makedirs(log_dir, exist_ok=True)
        self.logger: logging.Logger = logging.getLogger("FastAPI")
        self.logger.setLevel(level)
        
        log_path: str = os.path.join(log_dir, filename)
        handler = logging.FileHandler(log_path)
        formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s - %(endpoint)s - %(method)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
    def log_function(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.logger.info(f"{func.__name__} was called", extra={"endpoint": "/", "method": "GET"})
            result = func(*args, **kwargs)
            self.logger.info(f"{func.__name__} finished", extra={"endpoint": "/", "method": "GET"})
            return result
        return wrapper

logger: TextLogger = TextLogger()