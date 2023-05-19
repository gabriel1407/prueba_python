"""from celery.decorators import task
from celery.utils.log import get_task_logger
from time import sleep
logger = get_task_logger(__name__)
@task(name='my_first_task')
def my_first_task(duration):
    sleep(duration)
    return('first_task_done')"""
    
from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return 'Done!'