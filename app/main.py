from fastapi import FastAPI

app = FastAPI(title="Weight Tracker API")


@app.get("/api/health")
@app.get("/health")
def check_health() -> dict[str, str]:
    return {"status": "healthy"}
