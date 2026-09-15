from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import json
import sys
from pathlib import Path

app = FastAPI(title="ChainGuard AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

BASE_DIR = Path(__file__).resolve().parent
PIPELINE = BASE_DIR / "pipeline.py"

@app.get("/")
def home():
    return {
        "message": "ChainGuard AI API is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "ai": "connected"
    }

@app.post("/analyze")
def analyze(data: dict):
    process = subprocess.run(
        [sys.executable, str(PIPELINE)],
        input=json.dumps(data),
        text=True,
        capture_output=True,
        cwd=str(BASE_DIR)
    )

    if process.returncode != 0:
        return {
            "success": False,
            "error": process.stderr or process.stdout
        }

    try:
        return json.loads(process.stdout)
    except json.JSONDecodeError:
        return {
            "success": False,
            "error": "Invalid response from AI pipeline",
            "output": process.stdout
        }