#data.py
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
    @classmethod
    def from_dataframe(cls, df: pd.DataFrame) -> List['Question']:
        """Convert a DataFrame to a list of Question models"""
        records = df.to_dict(orient="records")
        return [cls.model_validate(record) for record in records]
    
    @staticmethod
    def to_dataframe(questions: List['Question']) -> pd.DataFrame:
        """Convert a list of Question models to a DataFrame"""
        return pd.DataFrame([q.model_dump() for q in questions])


df: pd.DataFrame = pd.read_excel(data_path, dtype=str)


df = df.fillna('')


records: List[Dict[str, Any]] = cast(
    List[Dict[str, Any]], 
    df.to_dict(orient="records")
)




#questions = [Question.model_validate(record) for record in records]
questions = Question.from_dataframe(df)


validated_df = Question.to_dataframe(questions)
__all__ = ['Question', 'questions', 'validated_df', 'df']

