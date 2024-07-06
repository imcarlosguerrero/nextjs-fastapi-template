from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def index():
    return {"message": "Hello World from FastAPI!"}