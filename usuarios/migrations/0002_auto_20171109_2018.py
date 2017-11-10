# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='titulo',
        ),
        migrations.AddField(
            model_name='user',
            name='biografia',
            field=models.CharField(max_length=255, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='fecha_inicio',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='gemas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='usuarios/perfiles/', default='usuarios/default/perfil.png'),
        ),
        migrations.AddField(
            model_name='user',
            name='nivel',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
