from __future__ import unicode_literals
from urlparse import urlparse

from BeautifulSoup import BeautifulStoneSoup
from django.shortcuts import get_object_or_404
import requests
import feedparser
from readability.readability import Document
from scrapy import Selector

from .models import Url


def request(url):
    r = requests.get(url)
    return r if r.status_code == 200 else False


def parse_sitemap(url):
    response = request(url)
    if not response:
        return response

    soup = BeautifulStoneSoup(response.content)
    urls = soup.findAll('url')
    if not urls:
        return False

    sitemap = list()
    for url in urls:
        sitemap.append(url.find('loc').string)
    return sitemap


def parse_rss(url):
    response = feedparser.parse(url)
    return [item.link for item in response.entries]


def parse_html(url):
    response = request(url)
    if not response:
        return response

    document = Document(response.content)
    doc = {
        'titulo': document.short_title(),
        'texto': document.summary(),
        'site': urlparse(url).netloc,
        'url': get_object_or_404(Url, url=url),
        'imagem': get_image(response.content, urlparse(url).netloc)
    }
    return doc


def get_image(article, site):
    hxs = Selector(text=article)
    try:
        image = hxs.xpath('//img/@src').extract()[0]
        if image[0] == '/':
            image = site + '/' + image
        return image
    except IndexError:
        return None