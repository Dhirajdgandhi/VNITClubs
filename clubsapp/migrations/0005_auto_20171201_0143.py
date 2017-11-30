# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubsapp', '0004_auto_20171201_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='photograph',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
