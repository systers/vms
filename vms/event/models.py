# Django
from django.core.validators import RegexValidator
from cities_light.models import City, Country, Region
from django.db import models


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=75,
        validators=[
            RegexValidator(
                r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\.)|(,)|(\-)|(!)|(\')]+$', ),
        ],
        )
    start_date = models.DateField()
    end_date = models.DateField()

    address = models.CharField(
        max_length=75,
        validators=[
            RegexValidator(r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\-)|(\')]+$', ),
        ],
        blank=True,
        null=True,
    )
    city = models.ForeignKey(City)
    state = models.ForeignKey(Region)
    country = models.ForeignKey(Country)
    venue = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(r'^[(A-Z)|(a-z)|(\s)|(\-)|(\')]+$', ),
        ],
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
