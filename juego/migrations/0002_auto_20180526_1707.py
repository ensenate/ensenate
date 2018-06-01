# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='puntuacion',
            name='juego',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='puntuacion',
            name='puntos',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
