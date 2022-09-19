from apscheduler.schedulers.blocking import BlockingScheduler

from settings import config


def my_function():
    print('test-function')


def schedule():
    scheduler = BlockingScheduler()
    params = config['Scheduler']
    scheduler.add_job(my_function, 'cron', **params)
    scheduler.start()


if __name__ == '__main__':
    schedule()