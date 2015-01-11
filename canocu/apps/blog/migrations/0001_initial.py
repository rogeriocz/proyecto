# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=300)),
                ('imagen', models.ImageField(upload_to=b'bloger')),
                ('contenido', models.TextField()),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('publicado', models.BooleanField(default=True)),
                ('creado', models.DateField(auto_now_add=True)),
                ('modificado', models.DateField(auto_now=True)),
                ('creador', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-creado'],
                'verbose_name': 'Blog Entrada',
                'verbose_name_plural': 'Blog Entradas',
            },
            bases=(models.Model,),
        ),
    ]
