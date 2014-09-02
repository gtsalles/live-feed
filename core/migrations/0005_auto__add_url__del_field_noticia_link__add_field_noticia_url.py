# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Url'
        db.create_table(u'core_url', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(unique=True, max_length=200)),
            ('status_processamento', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Url'])

        # Deleting field 'Noticia.link'
        db.delete_column(u'core_noticia', 'link')

        # Adding field 'Noticia.url'
        db.add_column(u'core_noticia', 'url',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Url'], unique=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Url'
        db.delete_table(u'core_url')

        # Adding field 'Noticia.link'
        db.add_column(u'core_noticia', 'link',
                      self.gf('django.db.models.fields.URLField')(default=None, max_length=200, unique=True, db_index=True),
                      keep_default=False)

        # Deleting field 'Noticia.url'
        db.delete_column(u'core_noticia', 'url_id')


    models = {
        u'core.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'data_insercao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_publicacao': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Site']"}),
            'subtitulo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_index': 'True'}),
            'url': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Url']", 'unique': 'True'})
        },
        u'core.site': {
            'Meta': {'object_name': 'Site'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'start': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'xpath_data': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'core.url': {
            'Meta': {'ordering': "['-data_criacao']", 'object_name': 'Url'},
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status_processamento': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['core']