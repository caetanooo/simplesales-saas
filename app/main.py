from fastapi import FastAPI  

app = FastAPI(tittle="Simplesales API") 

@app.get("/") 
def root(): 
    return {"message:" "SimpleSales API esta rodadndo"} 