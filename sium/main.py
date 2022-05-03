from fastapi import APIRouter, Depends, HTTPException, Header
from sium.schemas import E2wBarcodeModel
from sqlalchemy.orm import Session
from sium import crud, models
from database import SessionLocal, engine
from security import secret_token

models.Base.metadata.create_all(bind=engine)

app = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/E2S_Barcode/")
async def e2s_barcode(message: E2wBarcodeModel, db: Session = Depends(get_db)):
    # result = crud.get_barcode(db, 1)
    result = crud.create_barcode(db, message)
    return result

@app.get("/")
async def root():
    return {"message": "Hello World"}
