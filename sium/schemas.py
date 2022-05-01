from typing import List, Optional
from pydantic import BaseModel

class HeaderMsg(BaseModel):
    UUID: str
    EventID: str
    Direction: str
    SystemID: str

class E2wBarcodeModel(BaseModel):
    class E2wBarcodeMessage(BaseModel):

        class E2wBarcodeInfo(BaseModel):
            id_owner: str
            cod_item: str
            barcode: str
            sts_edit: int
            dat_create: str
            uuid: str

        Header: HeaderMsg
        Body: E2wBarcodeInfo

    Message: E2wBarcodeMessage
