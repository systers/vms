# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_remove_event_country2'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='country2',
            field=models.CharField(default=b'NZ', max_length=50, choices=[(b'FR', b'Freshman')]),
        ),
    ]
