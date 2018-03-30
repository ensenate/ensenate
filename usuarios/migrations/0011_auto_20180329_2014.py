# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_auto_20180329_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosunidadusuario',
            name='ultima_vez',
            field=models.DateField(null=True),
        ),
    ]
