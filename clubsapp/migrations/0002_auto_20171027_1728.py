# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='aboutUs',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='yearOfStart',
            field=models.IntegerField(max_length=6, null=True),
        ),
    ]
