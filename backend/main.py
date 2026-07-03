from fastapi import FastAPI

app = FastAPI(
    title="CAREGraph API",
    description="Backend for the CAREGraph Multi-Agent Healthcare System",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "CAREGraph Backend is Running!"
    }