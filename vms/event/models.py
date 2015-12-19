from django.core.validators import RegexValidator
from django.db import models

from django_countries.fields import CountryField
from django_countries import countries


class Event(models.Model):
    name = models.CharField(
        max_length=75,
        validators=[
            RegexValidator(
                r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\.)|(,)|(\-)|(!)|(\')]+$',
            ),
        ],
    )
    country2=models.CharField(default='NZ',max_length=50)
    
    start_date = models.DateField()
    end_date = models.DateField()

    address = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(
                r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\-)|(\')]+$',
            ),
        ],
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(
                r'^[(A-Z)|(a-z)|(\s)|(\-)|(\')]+$',
            ),
        ],
        blank=True,
        null=True,
    )
    state = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(
                r'^[(A-Z)|(a-z)|(\s)|(\-)]+$',
            ),
        ],
        blank=True,
        null=True,
    )
    country = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(
                r'^[(A-Z)|(a-z)|(\s)|(\-)|(\')]+$',
            ),
        ],
        blank=True,
        null=True,
    )

    venue = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(
                r'^[(A-Z)|(a-z)|(\s)|(\-)|(\')]+$',
            ),
        ],
        blank=True,
        null=True,
    )
