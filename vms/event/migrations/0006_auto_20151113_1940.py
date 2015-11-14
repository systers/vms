# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20151113_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='country2',
            field=models.CharField(max_length=50, choices=[(b'FR', b'Freshman')]),
        ),
    ]
