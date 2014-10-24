from django.template.defaultfilters import truncatewords_html, striptags
from rest_framework import serializers
from .models import Noticia


class NoticiaSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField('get_url')
    texto = serializers.SerializerMethodField('get_text')

    def get_url(self, obj):
        return obj.url.url

    def get_text(self, obj):
        return truncatewords_html(striptags(obj.texto), 50)

    class Meta:
        model = Noticia
        fields = ('titulo', 'site', 'link', 'texto', 'data_publicacao')