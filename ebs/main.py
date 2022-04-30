from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from database import erp_Session, erp_engine
from security import secret_token

app = APIRouter()

# Dependency
def get_db():
    db = erp_Session()
    try:
        yield db
    finally:
        db.close()


@app.post("/E2W_Barcode/")
async def e2w_barcode(message: W2eChekModel, db: Session = Depends(get_db), x_token: str = Header(...)):
    if x_token != secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")

    result = crud.create_check(db, message)
    return result


@app.get("/")
async def root():
    return {"message": "Hello World"}
