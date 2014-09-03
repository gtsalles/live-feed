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


def parse_html(url):
    response = request(url)
    if not response:
        return response

class HtmlExtractor():

    url = html = url_parsed = page_content = site = None

    def __init__(self, url):
        self.url = url
        self.url_parsed = requests.get(self.url, timeout=15)

    def main(self):
        self.html = self.url_parsed.content
        page_content = Document(self.html)
        article = page_content.summary()
        title = page_content.short_title().encode('utf-8')
        site = urlparse(self.url_parsed.url).netloc
        html = self.url_parsed.text
        return {'texto': article, 'titulo': title, 'subtitulo': self.get_subtitle(article),
                'foto': self.get_image(article), 'site': site, 'link': self.url_parsed.url,
                'html': html, 'data_publicacao': self.get_publish_date(html)}

    def get_publish_date(self, html):
        hxs = Selector(text=html)
        import dateutil.parser

        metas_tags = ['@property="article:published_time"', '@name="date"', '@itemprop="dateModified"']
        for i in metas_tags:
            out = hxs.xpath('//meta[%s]/@content' % i).extract()
            if len(out) > 0:
                return dateutil.parser.parse(out[0])

        return None

    def get_subtitle(self, article):
        hxs = Selector(text=article)
        if len(hxs.xpath('//p/text()').extract()[0]) < 200:
            return hxs.xpath('//p/text()').extract()[1]
        return hxs.xpath('//p/text()').extract()[0]

    def get_image(self, article):
        hxs = Selector(text=article)
        try:
            image = hxs.xpath('//img/@src').extract()[0]
            if image[0] == '/':
                image = self.site + '/' + image
            return image
        except IndexError:
            return None