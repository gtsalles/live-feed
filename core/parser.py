from __future__ import unicode_literals
from urlparse import urlparse

from BeautifulSoup import BeautifulStoneSoup
from django.shortcuts import get_object_or_404
from django.utils import timezone
import requests
import feedparser
from readability.readability import Document
from scrapy import Selector
from .models import Site, Url


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
        'data_publicacao': get_data(response.content, urlparse(url).netloc),
        'imagem': get_image(response.content, urlparse(url).netloc)
    }
    return doc


def get_data(html, site):
    import dateutil.parser

    hxs = Selector(text=html)

    if '180graus.com' in site:
        out = hxs.xpath('//div[@class="data"]/text()').extract()
        data = out[0].split(' - ')[-1].split(' ')
        o = data[0] + ' ' + data[-1]
        return dateutil.parser.parse(o, dayfirst=True, ignoretz=True)

    metas_tags = ['@property="article:published_time"', '@name="date"', '@itemprop="dateModified"',
                  '@name="shareaholic:article_published_time"']
    for i in metas_tags:
        out = hxs.xpath('//meta[%s]/@content' % i).extract()
        try:
            if len(out) > 0:
                return dateutil.parser.parse(out[0], dayfirst=True, ignoretz=True)
        except TypeError:
            pass
    extra_tags = ['//abbr[@class="date"]/@title', '//abbr[@class="published"]/text()',
                  '//div[@class="materia-data"]/p/text()', '//time/text()', '//p[@class="post-date"]/text()',
                  '//*[@class="data"]/text()', '//small[@class="autor bloco"]/*/text()']
    for i in extra_tags:
        out = hxs.xpath('%s' % i).extract()
        try:
            if len(out) > 0:
                return dateutil.parser.parse(out[0], dayfirst=True, ignoretz=True)
        except TypeError:
            pass
    return timezone.now()


def get_image(article, site):
    hxs = Selector(text=article)
    try:
        image = hxs.xpath('//img/@src').extract()[0]
        if image[0] == '/':
            image = site + '/' + image
        return image
    except IndexError:
        return None