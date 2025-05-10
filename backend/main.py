from fastapi import FastAPI
from api.claims import router as claims_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to InsureX.ai Backend API"}

app.include_router(claims_router, prefix="/claims")