from django.db import IntegrityError
from .models import Site, Url, Noticia
from .parser import parse_sitemap, parse_rss, parse_html
from celery.task import periodic_task, task
from datetime import timedelta


@periodic_task(run_every=timedelta(seconds=20), ignore_results=True)
def get_sites():
    sites = Site.objects.filter(status=True)
    # get_sitemap.delay(sites.filter(tipo='sitemap'))
    get_rss.delay(sites.filter(tipo='rss'))


@task
def get_sitemap(qs):
    for site in qs:
        urls = parse_sitemap(site.start)
        if urls:
            create_urls.delay(urls)


@task
def get_rss(qs):
    for site in qs:
        urls = parse_rss(site.start)
        create_urls.delay(urls)


@task
def create_urls(urls):
    for url in urls:
        Url.objects.get_or_create(url=url)


@periodic_task(run_every=timedelta(seconds=20))
def get_noticias():
    for url in Url.objects.filter(status_processamento=False)[:100]:
        parse_url.delay(url.url)


@task
def parse_url(url):
    doc = parse_html(url)
    insere_noticia(doc)


@task
def insere_noticia(doc):
    try:
        if doc:
            Noticia.objects.create(**doc)
    except IntegrityError:
        from django.db import connection
        connection._rollback()
        urls = Url.objects.filter(url=doc.get('link'))
        urls.update(status_processamento=True)