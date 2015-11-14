# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20151113_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='country2',
        ),
    ]
