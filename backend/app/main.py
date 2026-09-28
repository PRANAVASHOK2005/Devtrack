from fastapi import FastAPI

app = FastAPI(title="DevTrack API")


@app.get("/")
def root():
    return {
        "message": "Welcome to DevTrack API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
    