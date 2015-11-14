# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_event_country2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='country2',
            field=models.CharField(default=b'NZ', max_length=50),
        ),
    ]
