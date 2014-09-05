# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='site',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=150),
        ),
    ]
