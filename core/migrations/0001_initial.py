# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Site'
        db.create_table(u'core_site', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('start', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('formato_data', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Site'])

        # Adding model 'Noticia'
        db.create_table(u'core_noticia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=150, db_index=True)),
            ('subtitulo', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('imagem', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('texto', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, db_index=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Site'])),
            ('data_insercao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_publicacao', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Noticia'])


    def backwards(self, orm):
        # Deleting model 'Site'
        db.delete_table(u'core_site')

        # Deleting model 'Noticia'
        db.delete_table(u'core_noticia')


    models = {
        u'core.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'data_insercao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_publicacao': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Site']"}),
            'subtitulo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_index': 'True'})
        },
        u'core.site': {
            'Meta': {'object_name': 'Site'},
            'formato_data': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'start': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['core']