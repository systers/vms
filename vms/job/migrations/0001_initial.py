# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('event', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(\\s)|(\\')]+$")])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField(blank=True, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\.)|(,)|(\\-)|(!)|(\\')]+$")])),
                ('event', models.ForeignKey(to='event.Event')),
            ],
        ),
    ]
