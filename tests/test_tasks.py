from fastapi.testclient import TestClient
from run import app
from sqlalchemy import select
from database import SessionLocal,erp_Session
from tasks.models import PackingModel, PackingLineModel
from tasks.e2w_pcom import task_e2w_pcom
from ebs.e2w_barcode import task_e2w_barcode

session = SessionLocal();

def test_session():
    stmt = select(PackingModel.uuid, PackingLineModel.id).join(PackingModel.lines) .order_by(PackingLineModel.id.desc())
    print(stmt)
    rows = session.execute(stmt)
    if rows:
        assert True
    else:
        assert False


def test_task_e2w_pcom():
    result = task_e2w_pcom()
    assert type(result) == dict

def test_task_e2w_barcode():
    result = task_e2w_barcode()
    assert type(result) == dict



