# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_datosleccionusuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosleccionusuario',
            name='completo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='datosunidadusuario',
            name='completo',
            field=models.BooleanField(default=False),
        ),
    ]
