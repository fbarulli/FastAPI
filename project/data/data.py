import os
cwd = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(cwd, "questions_en.xlsx")

import pandas as pd
from pydantic import BaseModel, Field
from typing import Optional


print(f"Current working directory: {os.getcwd()}")
print(f"Files in directory: {os.listdir('.')}")

class Question(BaseModel):
    question : str
    subject : str
    use : str
    correct : str
    responseA : Optional[str] = None
    responseB : Optional[str] = None
    responseC : Optional[str] = None
    remark : Optional[str] = Field(default="")
    
    class Config:
        extra = "ignore"
        validate_assignment = True
    
df = pd.read_excel(data_path) # type: ignore[attr-defined]
df = df.fillna({}) # type: ignore[attr-defined]

data = df.to_dict(orient="records") # type: ignore[attr-defined]

