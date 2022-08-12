from apscheduler.schedulers.background import BackgroundScheduler
from scheduled_job import job

def start():
    scheduler = BackgroundScheduler(timezone='Europe/Moscow')
    scheduler.add_job(job.check_messages, 'interval', minutes=5)
    scheduler.start()