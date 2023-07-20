from fastapi import FastAPI

app = FastAPI()


#this is simple will return a jason format response whenever the api is called 
@app.get("/")
def root():
    return {"message": "Hello World"}
