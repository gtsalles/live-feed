from BeautifulSoup import BeautifulStoneSoup
import requests
import feedparser


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