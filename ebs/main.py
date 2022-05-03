from fastapi import APIRouter, Depends, HTTPException, Header
from ebs import e2w_barcode
from database import erp_Session
from security import secret_token

app = APIRouter()

# Dependency
def get_db():
    db = erp_Session()
    try:
        yield db
    finally:
        db.close()


@app.get("/E2W_Barcode/")
async def e2w_Barcode():
    result = e2w_barcode.get_message()
    # result = e2w_barcode.task_e2w_barcode()
    return result

@app.get("/")
async def root():
    return {"message": "Hello World"}
