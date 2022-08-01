import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
 
app = Celery('backend', backend='rpc://rabbitmq:5672', brocker='amqp://rabbitmq:5672')
app.config_from_object('django.conf:settings', namespace='CELERY') 
app.autodiscover_tasks() #(lambda: settings.INSTALLED_APPS)
