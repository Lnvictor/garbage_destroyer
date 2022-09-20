from apscheduler.schedulers.blocking import BlockingScheduler
import os
from datetime import datetime, timedelta

from settings import config


def clean():
    for item in os.scandir(config['Cleaning']['dir']):
        last_access = datetime.fromtimestamp(os.path.getatime(item))
        delta = datetime.now() - last_access
        
        if os.path.isfile(item) and delta.days > int(config['Cleaning']['time_diff_in_days']):
            os.remove(item)
            


def schedule():
    scheduler = BlockingScheduler()
    params = config['Scheduler']
    scheduler.add_job(clean, 'cron', **params)
    scheduler.start()


if __name__ == '__main__':
    schedule()