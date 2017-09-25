# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0006_auto_20170712_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_table',
            name='recentdate',
            field=models.DateField(default=datetime.date(2017, 9, 24)),
        ),
        migrations.AlterField(
            model_name='experience_internship',
            name='round1_text',
            field=models.ForeignKey(related_name='experience_internship_round1', blank=True, to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AlterField(
            model_name='experience_internship',
            name='round2_text',
            field=models.ForeignKey(related_name='experience_internship_round2', blank=True, to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AlterField(
            model_name='experience_internship',
            name='round3_text',
            field=models.ForeignKey(related_name='experience_internship_round3', blank=True, to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AlterField(
            model_name='experience_internship',
            name='round4_text',
            field=models.ForeignKey(related_name='experience_internship_round4', blank=True, to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AlterField(
            model_name='experience_internship',
            name='round5_text',
            field=models.ForeignKey(related_name='experience_internship_round5', blank=True, to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AlterField(
            model_name='experience_internship',
            name='round6_text',
            field=models.ForeignKey(related_name='experience_internship_round6', blank=True, to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AlterField(
            model_name='experience_internship',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 24, 13, 8, 30, 515000)),
        ),
        migrations.AlterField(
            model_name='experience_placement',
            name='round1_text',
            field=models.ForeignKey(related_name='experience_placement_round1', blank=True, to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AlterField(
            model_name='experience_placement',
            name='round2_text',
            field=models.ForeignKey(related_name='experience_placement_round2', blank=True, to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AlterField(
            model_name='experience_placement',
            name='round3_text',
            field=models.ForeignKey(related_name='experience_placement_round3', blank=True, to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AlterField(
            model_name='experience_placement',
            name='round4_text',
            field=models.ForeignKey(related_name='experience_placement_round4', blank=True, to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AlterField(
            model_name='experience_placement',
            name='round5_text',
            field=models.ForeignKey(related_name='experience_placement_round5', blank=True, to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AlterField(
            model_name='experience_placement',
            name='round6_text',
            field=models.ForeignKey(related_name='experience_placement_round6', blank=True, to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AlterField(
            model_name='experience_placement',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 24, 13, 8, 30, 515000)),
        ),
        migrations.AlterField(
            model_name='forgotpasskeys',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 24, 13, 8, 30, 531000)),
        ),
        migrations.AlterField(
            model_name='personinformation',
            name='createdondate',
            field=models.DateField(default=datetime.date(2017, 9, 24)),
        ),
    ]
