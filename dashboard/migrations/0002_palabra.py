# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Palabra',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('titulo', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='curso/palabras/')),
                ('leccion', models.ForeignKey(to='dashboard.Leccion')),
            ],
        ),
    ]
