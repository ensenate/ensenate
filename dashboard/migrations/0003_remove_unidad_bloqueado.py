# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_palabra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unidad',
            name='bloqueado',
        ),
    ]
