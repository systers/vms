# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20151113_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='country2',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
