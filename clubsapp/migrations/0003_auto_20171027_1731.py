# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubsapp', '0002_auto_20171027_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='yearOfStart',
            field=models.TextField(max_length=6, null=True),
        ),
    ]
