from celery.schedules import crontab

# import tasks
imports = (
    'tasks.add',
    "tasks.e2w_pcom",
    "tasks.e2w_barcode"
    )

# #Timezone
enable_utc = False
timezone = 'Asia/Taipei'

# Broker and Backend
broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/0'

worker_concurrency = 5

# 每分鐘執行一次
c1 = crontab()
# 每天凌晨十二點執行
c2 = crontab(minute=0, hour=0)
# 每十五分鐘執行一次
c3 = crontab(minute='*/15')
# 每週日的每一分鐘執行一次
c4 = crontab(minute='*', hour='*', day_of_week='sun')
# 每週三，五的三點，七點和二十二點沒十分鐘執行一次
c5 = crontab(minute='*/10', hour='3,17,22', day_of_week='thu,fri')

beat_schedule = {
    'add run every 60 seconds': {
        'task': 'add',
        'schedule': c1,
        'args': (33, 2)
    },
    'e2w_pcom run every 60 seconds': {
        'task': 'e2w_pcom',
        'schedule': c1
    },
    'e2w_barcode run every 60 seconds': {
        'task': 'e2w_barcode',
        'schedule': c1
    }
}

