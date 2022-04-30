from fastapi import APIRouter, Depends, HTTPException, Header
from wms.schemas import W2eChekModel
from sqlalchemy.orm import Session
from wms import crud, models
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


@app.post("/W2E_chek/")
async def w2e_chek(message: W2eChekModel, db: Session = Depends(get_db), x_token: str = Header(...)):
    if x_token != secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")

    result = crud.create_check(db, message)
    return result


@app.get("/")
async def root():
    return {"message": "Hello World"}




