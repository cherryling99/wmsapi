#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__CoreyTeng__'
import os
import logging
import uvicorn
from fastapi import FastAPI
from ebs import app_ebs
from sium import app_sium
from wms import app_wms
from mock_wms import app_mock_wms

secret_token = "coneofsilence"

FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, filename='wmsapi.log', filemode='a', format=FORMAT)

app = FastAPI(
    title='Jourdeness WMS API docs',
    description='佐登妮絲WMS API文件',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redocs',
)

app.include_router(app_ebs, prefix='/ebs', tags=['EBS->WMS API'])
app.include_router(app_wms, prefix='/wms', tags=['WMS->EBS API'])
app.include_router(app_sium, prefix='/sium', tags=['模擬WMS API'])
# app.include_router(app_mock_wms, prefix='/mock_wms', tags=['模擬wmsAPI'])

if __name__ == '__main__':
    if os.getenv('MODE') == "development":
        uvicorn.run('run:app', host='127.0.0.1', port=8000, reload=True, debug=True, workers=4)
    else:
        uvicorn.run('run:app', host='0.0.0.0', port=8000, reload=False, debug=False, workers=4)

