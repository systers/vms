# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(\\s)|(\\-)]+$')])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(\\s)|(\\-)]+$')])),
                ('address', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\-)]+$')])),
                ('city', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(\\s)|(\\-)]+$')])),
                ('state', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(\\s)|(\\-)]+$')])),
                ('country', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(\\s)|(\\-)]+$')])),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(b'^\\s*(?:\\+?(\\d{1,3}))?([-. (]*(\\d{3})[-. )]*)?((\\d{3})[-. ]*(\\d{2,4})(?:[-.x ]*(\\d+))?)\\s*$', message=b'Please enter a valid phone number')])),
                ('unlisted_organization', models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\-)|(:)]+$')])),
                ('email', models.EmailField(unique=True, max_length=45)),
                ('websites', models.TextField(blank=True, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(\\s)|(\\.)|(\\-)|(?)|(=)|(#)|(:)|(/)|(_)|(&)]+$')])),
                ('description', models.TextField(blank=True, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\.)|(,)|(\\-)|(!)]+$')])),
                ('resume', models.TextField(blank=True, validators=[django.core.validators.RegexValidator(b'^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\.)|(,)|(\\-)|(!)]+$')])),
                ('resume_file', models.FileField(max_length=75, upload_to=b'vms/resume/', blank=True)),
                ('reminder_days', models.IntegerField(default=1, blank=True, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)])),
                ('organization', models.ForeignKey(to='organization.Organization', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
