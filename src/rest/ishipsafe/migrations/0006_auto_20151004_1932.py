# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ishipsafe', '0005_subscribe_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='role',
            field=models.CharField(max_length=256),
        ),
    ]
