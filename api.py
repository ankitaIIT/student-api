from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

# Load student marks data from JSON file
with open("data.json", "r") as file:
    data = json.load(file)

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
def get_marks(name: list[str] = []):
    marks = [student["marks"] for student in data if student["name"] in name]
    return {"marks": marks}
