from sqlalchemy import Boolean, Column, Integer, String, DateTime
from database import erp_Base as Base

class barCode(Base):
    __tablename__ = 'jds_wms_barcodeinfo'
    id_owner = Column(String(20), nullable=False)
    cod_item = Column(String(20), nullable=False, primary_key=True)
    barcode = Column(String(50), nullable=False)
    sts_edit = Column(Integer, nullable=False, primary_key=True)
    dat_create = Column(String(8), nullable=False)


