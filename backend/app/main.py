from fastapi import FastAPI
from pydantic import BaseModel
from .api import endpoints

app = FastAPI()

app.include_router(endpoints.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}