# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\.)|(,)|(\\-)|(!)|(\\')]+$")])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('address', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\-)|(\\')]+$")])),
                ('city', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(\\s)|(\\-)|(\\')]+$")])),
                ('state', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(\\s)|(\\-)]+$')])),
                ('country2', django_countries.fields.CountryField(max_length=2)),
                ('country', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(\\s)|(\\-)|(\\')]+$")])),
                ('venue', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(\\s)|(\\-)|(\\')]+$")])),
            ],
        ),
    ]
