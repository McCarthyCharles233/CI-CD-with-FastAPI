from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LandingPageData(BaseModel):
    title: str
    description: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the landing page!"}

@app.post("/submit")
def submit_data(data: LandingPageData):
    return {"message": f"Data received: {data.title} - {data.description}"}
