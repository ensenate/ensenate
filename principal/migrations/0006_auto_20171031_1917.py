# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_auto_20171031_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
