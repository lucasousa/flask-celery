from celery import Celery


BROKER_URL = 'redis://redis:6379/0'
CELERY_BROKER_URL = BROKER_URL
CELERY_RESULT_BACKEND = BROKER_URL

celery = Celery('integration', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)