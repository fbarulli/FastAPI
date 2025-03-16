# FastAPI Request Methods Example

This guide demonstrates four ways to pass a "username" parameter to a FastAPI endpoint in a single application.

## Complete FastAPI Application with Examples

```python
from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()

# 1. Dynamic Routing (Path Parameters)
# Username is included directly in the URL path.
# Example: curl -X GET -i http://127.0.0.1:8000/user/path/johndoe
# Response: {"username": "johndoe", "method": "Dynamic Routing"}
# Best For: Resource identification, RESTful API design, required parameters
@app.get('/user/path/{username}')
def get_user_path(username: str):
    return {'username': username, 'method': 'Dynamic Routing'}

# 2. Query Strings
# Username is passed as a parameter in the URL after the question mark.
# Example: curl -X GET -i "http://127.0.0.1:8000/user/query?username=johndoe"
# Response: {"username": "johndoe", "method": "Query Strings"}
# Best For: Optional parameters, filtering, searching, and pagination
@app.get('/user/query')
def get_user_query(username: str):
    return {'username': username, 'method': 'Query Strings'}

# 3. Request Body
# Username is included in the JSON body of the request.
# Example: curl -X POST -i -H "Content-Type: application/json" -d '{"username":"johndoe"}' http://127.0.0.1:8000/user/body
# Response: {"username": "johndoe", "method": "Request Body"}
# Best For: Complex data submission, creating resources, or multiple parameters
class User(BaseModel):
    username: str

@app.post('/user/body')
def create_user_body(user: User):
    return {'username': user.username, 'method': 'Request Body'}

# 4. Request Headers
# Username is passed in the HTTP headers of the request.
# Example: curl -X GET -i -H "username: johndoe" http://127.0.0.1:8000/user/header
# Response: {"username": "johndoe", "method": "Request Headers"}
# Best For: Metadata, authentication tokens, API keys, and client information
@app.get('/user/header')
def get_user_header(username: str = Header()):
    return {'username': username, 'method': 'Request Headers'}