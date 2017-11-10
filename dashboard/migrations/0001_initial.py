# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('bloqueado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('bloqueado', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='curso/unidades/')),
            ],
        ),
        migrations.AddField(
            model_name='leccion',
            name='unidad',
            field=models.ForeignKey(to='dashboard.Unidad'),
        ),
    ]
