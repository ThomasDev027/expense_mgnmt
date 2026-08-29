from fastapi import FastAPI

app = FastAPI(
    title="Expense Manager API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Expense Manager API",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }
