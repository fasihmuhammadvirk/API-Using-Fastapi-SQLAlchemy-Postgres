
from fastapi import FastAPI

app = FastAPI()

#this only return the simple jason response
@app.get("/")
def root():
    return {"message": "Hello World"}


#it take a name as a argument and return the response with that specific name
@app.get("/greet/{name}")
def greet_name(name:str):
    return {"message": f"Hello {name}"}
