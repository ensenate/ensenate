# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_auto_20171031_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='fecha',
        ),
    ]
