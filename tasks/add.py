from app_celery import celery
import time


@celery.task(name='add')
def add(x, y):
    result = x + y
    time.sleep(5)
    return result
