import cx_Oracle
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

connstr = "oracle+cx_oracle://apps:apps@10.40.10.102:1521/test?encoding=UTF-8"
engine = create_engine(connstr)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base(engine)
