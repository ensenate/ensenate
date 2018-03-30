# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_auto_20180329_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosunidadusuario',
            name='ultima_vez',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
