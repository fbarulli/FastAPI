import os
import pandas as pd
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any, cast


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


df: pd.DataFrame = pd.read_excel(data_path, dtype=str)


df = df.fillna('')


records: List[Dict[str, Any]] = cast(
    List[Dict[str, Any]], 
    df.to_dict(orient="records")
)


print("First record:", records[0] if records else "No records found")

questions = [Question.model_validate(record) for record in records]

print(f"Successfully loaded {len(questions)} questions")