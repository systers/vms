# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cities_light', '0004_auto_20151226_0722'),
        ('organization', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(\\s)|(\\-)]+$')])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(\\s)|(\\-)]+$')])),
                ('address', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\-)]+$')])),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('unlisted_organization', models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\-)|(:)]+$')])),
                ('email', models.EmailField(unique=True, max_length=45)),
                ('websites', models.TextField(blank=True, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(\\s)|(\\.)|(\\-)|(?)|(=)|(#)|(:)|(/)|(_)|(&)]+$')])),
                ('description', models.TextField(blank=True, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\.)|(,)|(\\-)|(!)]+$')])),
                ('resume', models.TextField(blank=True, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\.)|(,)|(\\-)|(!)]+$')])),
                ('resume_file', models.FileField(max_length=75, upload_to=b'vms/resume/', blank=True)),
                ('reminder_days', models.IntegerField(default=1, blank=True, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)])),
                ('city', models.ForeignKey(to='cities_light.City')),
                ('country', models.ForeignKey(to='cities_light.Country')),
                ('organization', models.ForeignKey(to='organization.Organization', null=True)),
                ('state', models.ForeignKey(to='cities_light.Region')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
