# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0003_auto_20170301_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForgotPassKeys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=20, null=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2017, 7, 2, 10, 41, 25, 376905))),
            ],
        ),
        migrations.AlterField(
            model_name='company_table',
            name='recentdate',
            field=models.DateField(default=datetime.date(2017, 7, 2)),
        ),
        migrations.AlterField(
            model_name='experience_internship',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 2, 10, 41, 25, 375061)),
        ),
        migrations.AlterField(
            model_name='experience_placement',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 2, 10, 41, 25, 373412)),
        ),
        migrations.AlterField(
            model_name='personinformation',
            name='createdondate',
            field=models.DateField(default=datetime.date(2017, 7, 2)),
        ),
        migrations.AddField(
            model_name='forgotpasskeys',
            name='user',
            field=models.ForeignKey(to='portalapp.Personinformation', null=True),
        ),
    ]
