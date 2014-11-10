from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


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
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    imagem = models.TextField(blank=True, null=True)
    texto = models.TextField()
    site = models.CharField(max_length=100)
    url = models.ForeignKey('Url', db_index=True, unique=True)

    data_insercao = models.DateTimeField(auto_now_add=True)
    data_publicacao = models.DateTimeField(blank=True, null=True, default=timezone.now())

    def __unicode__(self):
        return self.titulo


@receiver(post_save, sender=Noticia)
def noticia_post_save(instance, **kwargs):
    url = instance.url
    url.status_processamento = True
    url.save()


class Url(models.Model):
    url = models.URLField(unique=True, max_length=400)
    status_processamento = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.url

    class Meta:
        ordering = ['-data_criacao']