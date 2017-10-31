# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20171031_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='fecha',
            field=models.DateField(auto_now=True, default=datetime.datetime(2017, 10, 31, 19, 6, 57, 734896, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
