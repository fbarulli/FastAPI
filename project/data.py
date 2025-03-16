from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    question : str
    subject : str
    use : str
    correct : str
    responseA : Optional[str] = None
    responseB : Optional[str] = None
    responseC : Optional[str] = None
    remark : Optional[str] = Field(default="")
    
df = pd.read_excel('data/questions_en.xlsx') #type: ignore
df = df.fillna(value=None) # type: ignore

data = df.to_dict(orient="records") # type: ignore

