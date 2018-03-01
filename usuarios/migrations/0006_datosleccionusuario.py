# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_unidad_bloqueado'),
        ('usuarios', '0005_auto_20180221_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosLeccionUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ultima_vez', models.DateField(default=django.utils.timezone.now)),
                ('bloqueado', models.BooleanField(default=True)),
                ('leccion', models.ForeignKey(to='dashboard.Leccion')),
                ('unidad', models.ForeignKey(to='dashboard.Unidad')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
