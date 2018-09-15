# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-10 17:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EditRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_hrs', models.DecimalField(decimal_places=2, max_digits=20)),
                ('confirm_status', models.IntegerField(default=0)),
                ('date_submitted', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('max_volunteers', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5000)])),
                ('address', models.CharField(blank=True, max_length=75, null=True, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\-)|(\\')]+$")])),
                ('venue', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(\\s)|(\\-)|(\\')]+$")])),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerShift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('date_logged', models.DateTimeField(blank=True, null=True)),
                ('edit_requested', models.BooleanField(default=False)),
                ('report_status', models.BooleanField(choices=[(False, b'Not reported'), (True, b'Reported')], default=False)),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shift.Shift')),
            ],
        ),
    ]
