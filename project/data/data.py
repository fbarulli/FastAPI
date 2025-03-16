import os
import pandas as pd
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

# Get path to the Excel file
cwd = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(cwd, "questions_en.xlsx")

class Question(BaseModel):
    question: str
    subject: str
    use: str
    correct: str
    responseA: Optional[str] = None
    responseB: Optional[str] = None
    responseC: Optional[str] = None
    remark: Optional[str] = Field(default="")
    
    class Config:
        extra = "ignore"
        validate_assignment = True


df = pd.read_excel(data_path)  # type: ignore


records = df.replace({pd.NA: None}).to_dict(orient="records")  # type: ignore


questions = [Question.model_validate(record) for record in records]

print(f"Successfully loaded {len(questions)} questions")