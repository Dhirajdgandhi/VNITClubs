# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubsapp', '0003_auto_20171204_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
