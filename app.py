#!/usr/bin/env python
from apscheduler.schedulers.blocking import BlockingScheduler
from garbage_destroyer.settings import config
from garbage_destroyer.clean import clean
            

def schedule():
    scheduler = BlockingScheduler()
    params = config['Scheduler']
    time_diff = int(config['Cleaning']['time_diff_in_days'])
    dir = config['Cleaning']['dir']
    ext = config['Cleaning'].get('file_extension')

    scheduler.add_job(clean, 'cron', (time_diff, ext, dir), **params)
    scheduler.start()


if __name__ == '__main__':
    schedule()
