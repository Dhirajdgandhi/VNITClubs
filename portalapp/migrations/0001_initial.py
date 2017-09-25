# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Department_Relation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('session', models.CharField(max_length=20, null=True)),
                ('intern_valid', models.IntegerField(default=0)),
                ('job_valid', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='company_table',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('company_name', models.TextField(null=True)),
                ('short_name', models.TextField(max_length=45, null=True)),
                ('long_name', models.TextField(max_length=45, null=True)),
                ('display_name', models.TextField(max_length=45, null=True)),
                ('intern_exp_count', models.IntegerField(default=1)),
                ('job_exp_count', models.IntegerField(default=1)),
                ('company_intern_valid', models.IntegerField(default=0)),
                ('company_job_valid', models.IntegerField(default=0)),
                ('startdate', models.DateTimeField()),
                ('recentdate', models.DateTimeField(default=datetime.datetime(2017, 2, 3, 14, 35, 16, 50966))),
                ('valid', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('short_name', models.TextField(max_length=45, null=True)),
                ('long_name', models.TextField(max_length=45, null=True)),
                ('display_name', models.TextField(max_length=45, null=True)),
                ('program', models.TextField(max_length=45, null=True)),
                ('degree_level', models.TextField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Difficulty_type',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('display_name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='experience_internship',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('criteria', models.CharField(max_length=500, null=True)),
                ('onoffcampus', models.IntegerField(default=1, max_length=5)),
                ('package', models.FloatField(null=True)),
                ('cgpa', models.FloatField(null=True)),
                ('num_of_rounds', models.IntegerField(default=0)),
                ('other_comments', models.TextField(default=b'')),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2017, 2, 3, 14, 35, 16, 56809))),
                ('valid', models.IntegerField(default=0)),
                ('cdr_id', models.ForeignKey(to='portalapp.Company_Department_Relation', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='experience_placement',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('criteria', models.CharField(max_length=500, null=True)),
                ('onoffcampus', models.IntegerField(default=1, max_length=5)),
                ('package', models.FloatField(null=True)),
                ('cgpa', models.FloatField(null=True)),
                ('num_of_rounds', models.IntegerField(default=0)),
                ('other_comments', models.TextField(default=b'')),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2017, 2, 3, 14, 35, 16, 55131))),
                ('valid', models.IntegerField(default=0)),
                ('cdr_id', models.ForeignKey(to='portalapp.Company_Department_Relation', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ForLogin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=500, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InterviewRound_details',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('time', models.IntegerField(default=0)),
                ('description', models.TextField(null=True)),
                ('difficulty', models.ForeignKey(to='portalapp.Difficulty_type')),
            ],
        ),
        migrations.CreateModel(
            name='InterviewRound_type',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('display_name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Personinformation',
            fields=[
                ('email', models.EmailField(max_length=100)),
                ('firstname', models.TextField(max_length=45, null=True)),
                ('lastname', models.TextField(max_length=45, null=True)),
                ('telephone1', models.CharField(max_length=15, null=True)),
                ('telephone2', models.CharField(max_length=15, null=True)),
                ('clg_id', models.IntegerField(max_length=5, serialize=False, primary_key=True)),
                ('deptid', models.IntegerField(max_length=5)),
                ('roll_no', models.TextField(max_length=10, null=True)),
                ('createdondate', models.DateTimeField()),
                ('is_active', models.IntegerField(default=0)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Profile_type',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('display_name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session', models.TextField(null=True)),
                ('status', models.IntegerField(default=0)),
                ('company_id', models.ForeignKey(to='portalapp.company_table', null=True)),
                ('intern_exp_id', models.ForeignKey(to='portalapp.experience_internship', null=True)),
                ('job_exp_id', models.ForeignKey(to='portalapp.experience_placement', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('role_id', models.AutoField(serialize=False, primary_key=True)),
                ('short_name', models.TextField(max_length=45, null=True)),
                ('long_name', models.TextField(max_length=45, null=True)),
                ('display_name', models.TextField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('display_name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='personinformation',
            name='roleid',
            field=models.ForeignKey(default=1, to='portalapp.Roles'),
        ),
        migrations.AddField(
            model_name='interviewround_details',
            name='round_type',
            field=models.ForeignKey(to='portalapp.InterviewRound_type'),
        ),
        migrations.AddField(
            model_name='forlogin',
            name='clg_id',
            field=models.ForeignKey(to='portalapp.Personinformation'),
        ),
        migrations.AddField(
            model_name='experience_placement',
            name='profile',
            field=models.ForeignKey(to='portalapp.Profile_type', null=True),
        ),
        migrations.AddField(
            model_name='experience_placement',
            name='round1_text',
            field=models.ForeignKey(related_name='experience_placement_round1', to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AddField(
            model_name='experience_placement',
            name='round2_text',
            field=models.ForeignKey(related_name='experience_placement_round2', to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AddField(
            model_name='experience_placement',
            name='round3_text',
            field=models.ForeignKey(related_name='experience_placement_round3', to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AddField(
            model_name='experience_placement',
            name='round4_text',
            field=models.ForeignKey(related_name='experience_placement_round4', to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AddField(
            model_name='experience_placement',
            name='round5_text',
            field=models.ForeignKey(related_name='experience_placement_round5', to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AddField(
            model_name='experience_placement',
            name='round6_text',
            field=models.ForeignKey(related_name='experience_placement_round6', to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AddField(
            model_name='experience_placement',
            name='userid',
            field=models.ForeignKey(to='portalapp.Personinformation'),
        ),
        migrations.AddField(
            model_name='experience_internship',
            name='profile',
            field=models.ForeignKey(to='portalapp.Profile_type', null=True),
        ),
        migrations.AddField(
            model_name='experience_internship',
            name='round1_text',
            field=models.ForeignKey(related_name='experience_internship_round1', to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AddField(
            model_name='experience_internship',
            name='round2_text',
            field=models.ForeignKey(related_name='experience_internship_round2', to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AddField(
            model_name='experience_internship',
            name='round3_text',
            field=models.ForeignKey(related_name='experience_internship_round3', to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AddField(
            model_name='experience_internship',
            name='round4_text',
            field=models.ForeignKey(related_name='experience_internship_round4', to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AddField(
            model_name='experience_internship',
            name='round5_text',
            field=models.ForeignKey(related_name='experience_internship_round5', to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AddField(
            model_name='experience_internship',
            name='round6_text',
            field=models.ForeignKey(related_name='experience_internship_round6', to='portalapp.InterviewRound_details', null=True),
        ),
        migrations.AddField(
            model_name='experience_internship',
            name='userid',
            field=models.ForeignKey(to='portalapp.Personinformation'),
        ),
        migrations.AddField(
            model_name='company_department_relation',
            name='company_id',
            field=models.ForeignKey(to='portalapp.company_table'),
        ),
        migrations.AddField(
            model_name='company_department_relation',
            name='deptid',
            field=models.ForeignKey(to='portalapp.Department'),
        ),
    ]
