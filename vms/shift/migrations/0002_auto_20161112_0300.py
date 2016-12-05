# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0001_initial'),
        ('volunteer', '0001_initial'),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteershift',
            name='volunteer',
            field=models.ForeignKey(to='volunteer.Volunteer'),
        ),
        migrations.AddField(
            model_name='shift',
            name='job',
            field=models.ForeignKey(to='job.Job'),
        ),
        migrations.AddField(
            model_name='shift',
            name='volunteers',
            field=models.ManyToManyField(to='volunteer.Volunteer', through='shift.VolunteerShift'),
        ),
    ]
