# coding: utf-8
from celery import Celery

app = Celery('qqq_ppp')

app.config_from_object('celery_config', namespace='CELERY')
if __name__ == '__main__':
    app._get_backend()