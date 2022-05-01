from typing import List, Optional
from pydantic import BaseModel

class W2eChekModel(BaseModel):

    class W2eChekInnerMessage(BaseModel):
        class W2eChekHeader(BaseModel):
            UUID: str
            EventID: str
            Direction: str
            SystemID: str

        class W2eChekBody(BaseModel):
            class W2eChekChekInfo(BaseModel):
                id_owner: str
                id_sub: str
                dat_chk: str
                num_chk: str
                no_ser: str
                cod_loc: str
                type_adj: str
                cod_item: str
                qty_stk: int
                qty_chk: int
                unt_stk: str
                ser_pcs_stk: str
                dat_expiry_stk: str
                ser_pcs_chk: str
                dat_expiry_chk: str
                type_error: Optional[str] = None

            chekInfo: List[W2eChekChekInfo]

        Header: W2eChekHeader
        Body: W2eChekBody

    Message: W2eChekInnerMessage
