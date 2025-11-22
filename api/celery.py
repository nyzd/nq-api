import os
from celery import Celery
from django.conf import settings
from kombu import Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

app = Celery('nq-api')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.task_queues = {
    'forced_alignment': {
        'exchange': 'forced_alignment',
        'routing_key': 'forcedalignment.processing',
    },
    'forced_alignment_done': {
        'exchange': 'forced_alignment_done',
        'routing_key': 'forcedalignment_done.processing',
    },
}

app.conf.task_routes = {
    'quran.tasks.forced_alignment': {
        'queue': 'forced_alignment',
        'routing_key': 'forcedalignment.processing',
    },
    'quran.tasks.forced_alignment_done': {
        'queue':'forced_alignment_done',
        'routing_key': 'forcedalignment_done.processing',
    }
}