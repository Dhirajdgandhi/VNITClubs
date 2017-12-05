# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubsapp', '0002_remove_club_fbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='heading',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
