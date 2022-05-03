import json
import uuid
import requests
from database import erp_Session
from .models import barCode

session = erp_Session()

def post_e2w_barcode(message, url):
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
    req_uuid = str(uuid.uuid4())
    header = {
        "UUID": req_uuid,
        "EventID": "E2W_Barcode",
        "Direction": "Primary",
        "SystemID": "ERP"
    }

    BarcodeInfo = []

    rows = session.query(barCode)
    for row in rows:
        dict_BarcodeInfo = {
            "id_owner": row.id_owner,
            "cod_item": row.cod_item,
            "barcode":  row.barcode,
            "sts_edit": row.sts_edit,
            "dat_create": row.dat_create
        }

        BarcodeInfo.append(dict_BarcodeInfo)

    message = {
        "Message": {
            "Header": header,
            "Body": {
                "BarcodeInfo": BarcodeInfo
            }
        }
    }
    # print(json.dumps(message))
    return message

def task_e2w_barcode():
    wms_url = "http://127.0.0.1:8000/sium"
    url = wms_url + "/E2S_Barcode/"
    message = get_message()
    response = post_e2w_barcode(message, url)
    return response

if __name__ == '__main__':
    # result = task_e2w_barcode()
    # print(result)
    #print(type(result))
    # test_session()
    message = get_message()
    print(message)
