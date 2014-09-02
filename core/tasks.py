from django.core.mail import send_mail

from feed.celery import app
from .models import Site


@app.task
def get_sites():
    for i in Site.objects.all():
        print i


@app.task
def send():
    send_mail('assunto', from_email='gt.salles@gmail.com', message='MENSAGEM', recipient_list=['gt.salles@gmail.com'])