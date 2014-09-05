import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from core.models import Url, Noticia


class NoticiasList(ListView):
    model = Noticia
    paginate_by = 10
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-data_publicacao')


def stats(request):
    context = dict()
    context['noticias'] = Noticia.objects.count()
    context['urls_total'] = Url.objects.count()
    context['urls_false'] = Url.objects.filter(status_processamento=False).count()
    return HttpResponse(json.dumps(context), content_type="application/json")


def monitor(request):
    return render(request, 'monitor.html')