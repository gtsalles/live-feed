from django.db import models


TIPO_CHOICES = (
    ('sitemap', 'Sitemap'),
    ('rss', 'RSS'),
    ('outro', 'Outro'),
)

class Site(models.Model):
    nome = models.CharField(max_length=50)
    site = models.URLField()
    start = models.URLField()
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    status = models.BooleanField(default=True)
    formato_data = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.nome


class Noticia(models.Model):
    titulo = models.CharField(max_length=150, db_index=True)
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    imagem = models.TextField(blank=True, null=True)
    texto = models.TextField()
    link = models.URLField(db_index=True)
    site = models.ForeignKey('Site')

    data_insercao = models.DateTimeField(auto_now_add=True)
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.titulo
