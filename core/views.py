# coding=utf-8
import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from core.models import Url, Noticia
from core.serializers import NoticiaSerializer


def home(request):
    return render(request, 'index.html')


def stats(request):
    context = dict()
    context['noticias'] = Noticia.objects.count()
    context['urls_total'] = Url.objects.count()
    context['urls_false'] = Url.objects.filter(status_processamento=False).count()
    return HttpResponse(json.dumps(context), content_type="application/json")


def monitor(request):
    return render(request, 'monitor.html')


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.order_by('-data_publicacao')
    serializer_class = NoticiaSerializer
    paginate_by = 10