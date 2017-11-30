# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubsapp', '0003_auto_20171027_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventphotorelationship',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventphotorelationship',
            name='photo',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='displayName',
            new_name='heading',
        ),
        migrations.RemoveField(
            model_name='clubmember',
            name='post',
        ),
        migrations.RemoveField(
            model_name='event',
            name='longName',
        ),
        migrations.RemoveField(
            model_name='event',
            name='shortName',
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='photos',
            name='details',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='photos',
            name='photograph',
            field=models.ImageField(null=True, upload_to=b'photos', blank=True),
        ),
        migrations.DeleteModel(
            name='EventPhotoRelationship',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
