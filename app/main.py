from fastapi import FastAPI 
from app.database import engine 
from app.models import Base 

app = FastAPI(title="SaaS MVP API") 

Base.metadata.create_all(bind=engine) 

app.get("/") 
def root(): 
    return {"status": "API running"} 

