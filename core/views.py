import json
from django.http import HttpResponse
from django.shortcuts import render
from core.models import Url, Noticia


def home(request):
    return render(request, 'base.html')


def stats(request):
    context = dict()
    context['noticias'] = Noticia.objects.count()
    context['urls_total'] = Url.objects.count()
    context['urls_false'] = Url.objects.filter(status_processamento=False).count()
    return HttpResponse(json.dumps(context), content_type="application/json")


def monitor(request):
    return render(request, 'monitor.html')