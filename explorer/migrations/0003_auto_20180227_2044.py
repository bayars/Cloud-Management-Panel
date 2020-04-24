# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0002_servers_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers',
            name='path',
            field=models.CharField(default=b'/home/username/', max_length=50),
        ),
    ]
