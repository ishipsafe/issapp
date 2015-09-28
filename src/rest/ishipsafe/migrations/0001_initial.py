# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceListing',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=10)),
                ('weight', models.IntegerField()),
                ('value', models.CharField(max_length=15)),
                ('price', models.DecimalField(max_digits=10, decimal_places=3)),
            ],
        ),
    ]
