# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_user_cargar_datos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosleccionusuario',
            name='leccion',
        ),
        migrations.RemoveField(
            model_name='datosleccionusuario',
            name='unidad',
        ),
        migrations.RemoveField(
            model_name='datosleccionusuario',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='DatosLeccionUsuario',
        ),
    ]
