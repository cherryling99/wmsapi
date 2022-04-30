from fastapi.testclient import TestClient
from run import app

client = TestClient(app)

message = {"Message": {
    "Header": {
        "UUID": "string",
        "EventID": "string",
        "Direction": "string",
        "SystemID": "string"
    },
    "Body": {
        "chekInfo": [
            {
                "id_owner": "string",
                "id_sub": "string",
                "dat_chk": "string",
                "num_chk": "string",
                "no_ser": "string",
                "cod_loc": "string",
                "type_adj": "string",
                "cod_item": "string",
                "qty_stk": 0,
                "qty_chk": 0,
                "unt_stk": "string",
                "ser_pcs_stk": "string",
                "dat_expiry_stk": "string",
                "ser_pcs_chk": "string",
                "dat_expiry_chk": "string",
                "type_error": "string"
            }
        ]
    }
}
}


def test_w2e_chek():
    response = client.post(
        "/wms/W2E_chek/",
        headers={"X-Token": "coneofsilence"},
        json=message,
    )
    assert response.status_code == 200


def test_w2e_chek_token():
    response = client.post(
        "/wms/W2E_chek/",
        headers={"X-Token": "hailhydra"},
        json=message,
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}


