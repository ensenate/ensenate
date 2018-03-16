# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20180302_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cargar_datos',
            field=models.BooleanField(default=False),
        ),
    ]
