from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def hello():
   return {"message": "Welcome to the Tea API!"}

@app.get("/home")
def home():
   return {"message": "Welcome to the Home Page!"}

@app.get("/about")
def about():
    return {"message": "Welcome to the About Page!"}