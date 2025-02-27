import os
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from transformers import pipeline

# Define request model with Pydantic
class CodeRequest(BaseModel):
    code: str

# Define response model
class AnalysisResponse(BaseModel):
    complexity: float
    errors: int
    readability: float

app = FastAPI()


# Get allowed origins from environment or use defaults
allowed_origins = os.environ.get("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins, # React's port
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/analyze", response_model=AnalysisResponse)
def analyze_code(request: CodeRequest):
    # Get the code from the request
    code = request.code

    # Dummy analysis TODO replace with real analysis later
    complexity = len(code) / 100  # Just a dummy placeholder complexity metric
    
    errors = code.count(';')  # Simple error check since python doesn't have semicolons
    
    readability = max(0, 10 - complexity)  # Just a dummy placeholder readability metric
    
    return {
        'complexity': round(complexity, 2),
        'errors': errors,
        'readability': round(readability, 2)
    }

# Add this if you want to run it directly with Python
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)