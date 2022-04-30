import os
import cx_Oracle
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

connstr = "oracle+cx_oracle://apps:apps@10.40.10.102:1521/test?encoding=UTF-8"
erp_engine = create_engine(connstr)
erp_Session = sessionmaker(autocommit=False, autoflush=False, bind=erp_engine)
erp_Base = declarative_base(erp_engine)
