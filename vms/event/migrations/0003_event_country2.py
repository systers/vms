# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_remove_event_country2'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='country2',
            field=django_countries.fields.CountryField(default=b'NZ', max_length=2),
        ),
    ]
