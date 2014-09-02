from .models import Site, Url
from .parser import parse_sitemap, parse_rss
from celery.task import periodic_task, task
from datetime import timedelta


@periodic_task(run_every=timedelta(seconds=60), ignore_results=True)
def get_sites():
    sites = Site.objects.filter(status=True)
    get_sitemap.delay(sites.filter(tipo='sitemap'))
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