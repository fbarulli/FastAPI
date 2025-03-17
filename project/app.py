from fastapi import FastAPI, HTTPException
from project.data.data import questions
from typing import List

app = FastAPI()  

#!curl -X GET "http://127.0.0.1:8000/questions"
@app.get("/questions") 
async def get_all_questions():     
    '''     
    returns : dict with all questions     
    '''
    try:
        return {"questions": [q.model_dump() for q in questions]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get questions: {str(e)}")


# !curl -X GET "http://127.0.0.1:8000/questions/use"
@app.get("/questions/use") 
async def get_all_uses():     
    '''     
    returns : dict with all uses     
    '''
    try:
        unique_uses = list(set(q.use for q in questions))
        return {"uses": unique_uses}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get uses: {str(e)}")

# !curl -X GET "http://127.0.0.1:8000/questions/Validation%20test"
@app.get('/questions/{use}') 
async def get_questions_by_use(use: str):     
    '''     
    returns : dict filtered by use     
    '''
    try:
        questions_by_use = [q.model_dump() for q in questions if q.use == use]
        return {"questions_by_use": questions_by_use}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get questions by use: {str(e)}")
    
@app.get("/questions/")
async def get_subjects(subjects: List[str]):
    '''
    Returns: dict with questions for the specified subjects
    Requires: At least one subject to be provided via query parameters
    Example: /questions/?subjects=math&subjects=science
    '''
    try:
        # Convert subjects to lowercase for case-insensitive comparison
        subjects_set = set(map(str.lower, subjects))

        # Filter questions by subjects using a set intersection and dict grouping
        matching_subjects = {
            subj: list(filter(lambda q: eq(q.subject.lower(), subj.lower()), questions))
            for subj in subjects_set
        }

        # Convert question objects to dictionaries for the response
        result = {subj: [q.__dict__ for q in qs] for subj, qs in matching_subjects.items()}

        # Check if any subjects matched
        if not any(result.values()):
            raise HTTPException(status_code=404, detail="No matching subjects found")

        return {"subjects": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get subjects: {str(e)}")