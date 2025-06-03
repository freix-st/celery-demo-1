from celery import Celery
from celery.schedules import crontab

app = Celery('scheduler')

app.conf.timezone = 'Asia/Shanghai'

# daily
app.conf.beat_schedule = {
    'daily-script-9am': {
        'task': 'tasks.run_daily_script',
        'schedule': crontab(hour=9, minute=0, day_of_week='mon-fri'),
    },
    'every-4-hours': {
        'task': 'tasks.generate_report',
        'schedule': crontab(hour='*/4', minute=0, day_of_week='mon-fri'),
    },
}