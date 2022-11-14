import glob
import os
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from garbage_destroyer.settings import config


def clean():
    file_extension = config['Cleaning'].get('file_extension')
    path = f"{config['Cleaning']['dir']}/*"

    if file_extension:
        path += f'.{file_extension}'

    for item in glob.glob(path):
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
