# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('boxname', models.CharField(unique=True, max_length=15)),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('port', models.PositiveIntegerField(default=22)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
