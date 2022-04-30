from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base


class PackingModel(Base):
    __tablename__ = "packing"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(255))
    date = Column(DateTime)
    uuid = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    lines = relationship("PackingLineModel", back_populates="packing")


class PackingLineModel(Base):
    __tablename__ = "packing_line"
    id = Column(Integer, primary_key=True, autoincrement=True)
    item_no = Column(String, index=True)
    qty = Column(Integer)
    description = Column(String, index=True)
    packing_id = Column(Integer, ForeignKey("packing.id"))

    packing = relationship("PackingModel", back_populates="lines")
