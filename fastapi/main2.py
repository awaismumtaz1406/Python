import json
from fastapi import FastAPI
app= FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "Welcome to the Tea API!"}

@app.get("/home")
def home():
    return {"message": "Welcome to the Home Page!"}

@app.get("/about")
def about():
    return {"message": "Welcome to the About Page!"}


@app.get('/view')
def view():
    data = load_data()
    return data