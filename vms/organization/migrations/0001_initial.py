# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=75, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\-)|(:)|(\\')]+$")])),
            ],
        ),
    ]
