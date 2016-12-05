# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('max_volunteers', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5000)])),
                ('address', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\-)|(\\')]+$")])),
                ('city', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(\\s)|(\\-)|(\\')]+$")])),
                ('state', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(\\s)|(\\-)]+$')])),
                ('country', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(\\s)|(\\-)|(\\')]+$")])),
                ('venue', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(\\s)|(\\-)|(\\')]+$")])),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerShift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.TimeField(null=True, blank=True)),
                ('end_time', models.TimeField(null=True, blank=True)),
                ('shift', models.ForeignKey(to='shift.Shift')),
            ],
        ),
    ]
