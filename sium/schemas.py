from typing import List, Optional
from pydantic import BaseModel

class E2wBarcodeModel(BaseModel):

    class E2wBarcodeMessage(BaseModel):
        class E2wBarcodeHeader(BaseModel):
            UUID: str
            EventID: str
            Direction: str
            SystemID: str

        class E2wBarcodeBody(BaseModel):
            class E2wBarcodeInfo(BaseModel):
                id_owner: str
                cod_item: str
                barcode: str
                sts_edit: int
                dat_create: str

            BarcodeInfo: List[E2wBarcodeInfo]

        Header: E2wBarcodeHeader
        Body: E2wBarcodeBody

    Message: E2wBarcodeMessage
