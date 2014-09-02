from haystack import indexes
from .models import Noticia


class NoticiaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    titulo = indexes.CharField(model_attr='titulo')
    subtitulo = indexes.CharField(model_attr='subtitulo')
    texto = indexes.CharField(model_attr='texto')
    link = indexes.CharField(model_attr='link')
    data_publicacao = indexes.DateTimeField(model_attr='data_publicacao')

    def get_model(self):
        return Noticia

    def get_updated_field(self):
        return 'data_publicacao'

    def index_queryset(self, using=None):
        return self.get_model().objects.all()