# logger.py
import logging
import os
from functools import wraps
from typing import Callable, Any


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
        
    @staticmethod
    def log_function(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger_instance = logging.getLogger("FastAPI")  # Adjust as needed
            logger_instance.info(f"{func.__name__} called", extra={"endpoint": "/", "method": "GET"})
            logger_instance.info(f"{func.__name__} finished", extra={"endpoint": "/", "method": "GET"})
            result = await func(*args, **kwargs)
            return result
        return wrapper
                
logger: TextLogger = TextLogger()