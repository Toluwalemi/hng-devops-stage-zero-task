from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the static directory to serve the static files
app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/api")
async def root():
    return {"message": "Hello World"}
