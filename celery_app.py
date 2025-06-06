from celery import Celery
from celery.schedules import crontab

app = Celery('scheduler')

app.conf.update(
    broker_url='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/0',
    timezone='Asia/Singapore',
)

# daily
app.conf.update(
    beat_schedule = {
        'daily-script-9am': {
            'task': 'tasks.run_daily_script',
            'schedule': crontab(hour=9, minute=0, day_of_week='mon-fri'),
        },
        'every-4-hours': {
            'task': 'tasks.generate_report',
            'schedule': crontab(hour='*/4', minute=0, day_of_week='mon-fri'),
        },
    },
    include=['tasks']
)