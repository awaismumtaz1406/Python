import json
from fastapi import FastAPI, HTTPException,Path
app= FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data


@app.get('/patients/{patient_id}')
def view_patient(patient_id: int = Path(...,
description="The ID of the patient to retrieve")):
    data = load_data()
    for patients in data:

        if patients["patient_id"] == patient_id:
            return patients
    raise HTTPException(status_code=404, detail="Patient not found")

