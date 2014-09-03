# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=150, db_index=True)),
                ('subtitulo', models.CharField(max_length=200, null=True, blank=True)),
                ('imagem', models.TextField(null=True, blank=True)),
                ('texto', models.TextField()),
                ('data_insercao', models.DateTimeField(auto_now_add=True)),
                ('data_publicacao', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('site', models.URLField()),
                ('start', models.URLField()),
                ('tipo', models.CharField(max_length=15, choices=[('sitemap', 'Sitemap'), ('rss', 'RSS'),
                                                                  ('outro', 'Outro')])),
                ('status', models.BooleanField(default=True)),
                ('xpath_data', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(unique=True, max_length=400)),
                ('status_processamento', models.BooleanField(default=False)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-data_criacao'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='noticia',
            name='site',
            field=models.ForeignKey(to='core.Site'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='noticia',
            name='url',
            field=models.ForeignKey(to='core.Url', unique=True),
            preserve_default=True,
        ),
    ]
