from sqlalchemy import Column, Integer, String
from database import Base

class BarcodeModel(Base):
    __tablename__ = "barcode"

    id_seq = Column(Integer, primary_key=True, autoincrement=True)
    id_owner = Column(String(20), nullable=False)
    cod_item = Column(String(20), nullable=False, unique = True)
    barcode = Column(String(50), nullable=False)
    sts_edit = Column(Integer, nullable=False)
    dat_create = Column(String(8), nullable=False)
    uuid = Column(String(128), nullable=False)