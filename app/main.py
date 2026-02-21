from fastapi import FastAPI
from app.routers import data_router

app = FastAPI(title="Lab Data Processor API")

app.include_router(data_router.router)

@app.get("/")
def root():
    return {"message": "Lab Data Processor API is running"}