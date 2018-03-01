# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20180209_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=30)),
                ('bloqueado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Palabra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to=b'curso/palabras/')),
                ('leccion', models.ForeignKey(to='usuarios.Leccion')),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=30)),
                ('bloqueado', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to=b'curso/unidades/')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='leccion',
            name='unidad',
            field=models.ForeignKey(to='usuarios.Unidad'),
        ),
    ]
