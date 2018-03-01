# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_palabra'),
        ('usuarios', '0004_auto_20180221_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosUnidadUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ultima_vez', models.DateField(default=django.utils.timezone.now)),
                ('fuerza', models.PositiveSmallIntegerField(default=0)),
                ('bloqueado', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='leccion',
            name='unidad',
        ),
        migrations.RemoveField(
            model_name='palabra',
            name='leccion',
        ),
        migrations.RemoveField(
            model_name='unidad',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Leccion',
        ),
        migrations.DeleteModel(
            name='Palabra',
        ),
        migrations.DeleteModel(
            name='Unidad',
        ),
        migrations.AddField(
            model_name='datosunidadusuario',
            name='unidad',
            field=models.ForeignKey(to='dashboard.Unidad'),
        ),
        migrations.AddField(
            model_name='datosunidadusuario',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
