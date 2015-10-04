# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ishipsafe', '0004_auto_20151004_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='role',
            field=models.CharField(default=b'flyer', max_length=256),
        ),
    ]
