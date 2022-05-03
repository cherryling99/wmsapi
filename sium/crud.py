import uuid
import datetime
from sqlalchemy.orm import Session
from . import schemas, models

def get_barcode(db: Session, id_Seq: int):
    return db.query(models.BarcodeModel).filter(models.BarcodeModel.id_seq == id_Seq).first()

def create_barcode(db: Session, barCode: schemas.E2wBarcodeModel):
    for item in barCode.Message.Body.BarcodeInfo:
        db_check = models.BarcodeModel()
        db_check.id_owner = item.id_owner
        db_check.cod_item = item.cod_item
        db_check.barcode = item.barcode
        db_check.sts_edit = item.sts_edit
        db_check.dat_create = item.dat_create
        db_check.uuid = barCode.Message.Header.UUID

        db.add(db_check)
        db.flush()

    result = {
        "Message": {
            "Header": {
                "UUID": db_check.uuid,
                "EventID": "E2W_Barcode",
                "Direction": "Secondary",
                "SystemID": "WMS"
            },
            "Body": {
                "ResultInfo": {
                    "Result": "True",
                    "ResultMessage": "Success"
                }
            }
        }
    }

    db.commit()
    return result

