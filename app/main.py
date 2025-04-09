# main.py

from fastapi import FastAPI
import pandas as pd
import openai
import os

# Initialize FastAPI app
app = FastAPI()

# Root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "Welcome to the SHL Assessment Recommendation System!"}

# Example endpoint: Fetching SHL assessment data from a CSV file
@app.get("/assessments")
def get_assessments():
    # Replace 'shl_assessments.csv' with the actual path to your CSV file
    df = pd.read_csv("shl_assessments.csv")
    assessments = df.to_dict(orient="records")
    return {"assessments": assessments}

# Example endpoint: Using OpenAI for a recommendation based on a query
@app.post("/recommend")
def recommend_assessment(query: str):
    # Example usage of OpenAI API (ensure you set your OpenAI API key in environment variables)
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    # You can customize this prompt based on your use case
    prompt = f"Given the job description or query: {query}, recommend relevant SHL assessments."
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the appropriate engine
        prompt=prompt,
        max_tokens=150
    )
    
    recommendation = response.choices[0].text.strip()
    return {"recommendation": recommendation}

# You can add more endpoints as needed for your specific use case
