# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_auto_20151114_0651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='country2',
        ),
    ]
