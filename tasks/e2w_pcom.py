import json
import requests
from sqlalchemy import select
from app_celery import celery
from database import SessionLocal
from .models import PackingModel, PackingLineModel

session = SessionLocal()

def post_e2w_pcom(message, url):
    response = requests.post(
                   url,
                   data=json.dumps(message),
                   headers={
                       "Content-Type": "application/json",
                       "Authorization": "XXX"
                   }
               )
    response = response.json()
    return response


def get_message():
    header = {
        "UUID": "UUID",
        "EventID": "E2W_Pcom",
        "Direction": "Primary",
        "SystemID": "ERP"
    }

    pcomdtlinfo = []
    pcominfo = {}

    stmt = select(PackingModel.uuid, PackingLineModel.id).join(PackingModel.lines) .order_by(PackingLineModel.id.desc())
    print(stmt)
    rows = session.execute(stmt)
    for row in rows:
        dict_pcomdtlinfo = {
            "lin_fabm": row.uuid,
            "cod_item": row.id,
            "typ_supy": "typ_supy",
            "qty_fabm": "qty_fabm",
            "unt_stk": "unt_stk",
            "ser_pcs": "ser_pcs",
            "dat_expiry": "dat_expiry"
        }

        pcomdtlinfo.append(dict_pcomdtlinfo)

        pcominfo = {
            "id_owner": "id_owner",
            "id_sub": "id_sub",
            "typ_fabm": "typ_fabm",
            "num_fabm": "num_fabm",
            "dat_fabm": "dat_fabm",
            "PcomDTLInfo": pcomdtlinfo
        }

    _message = {
        "Message": {
            "Header": header,
            "Body": {
                "PcomInfo": pcominfo
            }
        }
    }
    print(json.dumps(_message))
    return _message


@celery.task(name='e2w_pcom')
def task_e2w_pcom():
    wms_url = "http://127.0.0.1:8000/mock_wms"
    url = wms_url + "/E2W_Pcom/"
    message = get_message()
    response = post_e2w_pcom(message, url)
    return response


if __name__ == '__main__':
    result = task_e2w_pcom()
    print(result)
    print(type(result))
    # test_session()


