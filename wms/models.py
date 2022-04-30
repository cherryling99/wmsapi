from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base


class CheckModel(Base):
    __tablename__ = "check"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(255))
    date = Column(DateTime)
    uuid = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    lines = relationship("CheckLineModel", back_populates="check")


class CheckLineModel(Base):
    __tablename__ = "check_line"

    id = Column(Integer, primary_key=True, autoincrement=True)
    item_no = Column(String, index=True)
    qty = Column(Integer)
    description = Column(String, index=True)
    check_id = Column(Integer, ForeignKey("check.id"))

    check = relationship("CheckModel", back_populates="lines")
