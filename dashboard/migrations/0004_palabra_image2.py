# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_unidad_bloqueado'),
    ]

    operations = [
        migrations.AddField(
            model_name='palabra',
            name='image2',
            field=models.ImageField(default=b'curso/palabras/no-imagen.jpg', null=True, upload_to=b'curso/palabras/', blank=True),
        ),
    ]
