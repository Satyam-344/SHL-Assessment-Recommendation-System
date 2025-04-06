from fastapi import FastAPI
from pydantic import BaseModel
import openai
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI()

# Load OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the assessment data
assessments_df = pd.read_csv('data/shl_assessments.csv')

class Query(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the SHL Assessment Recommendation System!"}

@app.post("/recommend")
def recommend_assessments(query: Query):
    # Implement recommendation logic based on query
    return {"recommendations": "List of recommended assessments based on the query"}
