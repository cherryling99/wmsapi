import uuid
import datetime
from sqlalchemy.orm import Session
from . import schemas, models


def get_check(db: Session, check_id: int):
    return db.query(models.CheckModel).filter(models.CheckModel.id == check_id).first()


def create_check(db: Session, chek: schemas.W2eChekModel):
    """
    todo: 出錯還是要回傳符合格式的訊息
    要做try except處理
    """
    db_check = models.CheckModel()

    # db_check.uuid = chek.Message.Header.UUID
    db_check.uuid = uuid.uuid4()
    db_check.type = chek.Message.Header.EventID
    db_check.date = datetime.date.today()
    db.add(db_check)
    db.flush()

    for item in chek.Message.Body.chekInfo:
        db_check_line = models.CheckLineModel()
        db_check_line.check_id = db_check.id
        db_check_line.item_no = item.cod_item
        db_check_line.qty = item.qty_stk
        db.add(db_check_line)

    result = {
        "Message": {
            "Header": {
                "UUID": db_check.uuid,
                "EventID": "E2W_Pcom",
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
