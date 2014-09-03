from django.db import models


TIPO_CHOICES = (
    (u'sitemap', u'Sitemap'),
    (u'rss', u'RSS'),
    (u'outro', u'Outro'),
)


class Site(models.Model):
    nome = models.CharField(max_length=50)
    site = models.URLField()
    start = models.URLField()
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES)
    status = models.BooleanField(default=True)
    xpath_data = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.nome


class Noticia(models.Model):
    titulo = models.CharField(max_length=150, db_index=True)
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    imagem = models.TextField(blank=True, null=True)
    texto = models.TextField()
    site = models.ForeignKey('Site')
    url = models.ForeignKey('Url', db_index=True, unique=True)

    data_insercao = models.DateTimeField(auto_now_add=True)
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.titulo


class Url(models.Model):
    url = models.URLField(unique=True, max_length=400)
    status_processamento = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.link

    class Meta:
        ordering = ['-data_criacao']