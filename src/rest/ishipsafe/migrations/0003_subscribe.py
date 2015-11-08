# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ishipsafe', '0002_auto_20150920_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscribe',
            fields=[
                ('subscribe_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('email', models.CharField(max_length=256)),
            ],
        ),
    ]
