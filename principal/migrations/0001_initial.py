# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('asunto', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mensaje', models.TextField(max_length=350)),
            ],
        ),
    ]
