# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servers',
            name='path',
            field=models.CharField(default=b'/home/safa/', max_length=50),
        ),
    ]
