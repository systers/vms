# Django
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models
from datetime import datetime
# local Django
from job.models import Job
from volunteer.models import Volunteer


class Shift(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_volunteers = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(5000)])
    address = models.CharField(
        max_length=75,
        validators=[
            RegexValidator(r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\-)|(\')]+$', ),
        ],
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=75,
        validators=[
            RegexValidator(r'^[(A-Z)|(a-z)|(\s)|(\-)|(\')]+$', ),
        ],
        blank=True,
        null=True,
    )
    state = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(r'^[(A-Z)|(a-z)|(\s)|(\-)]+$', ),
        ],
        blank=True,
        null=True,
    )
    country = models.CharField(
        max_length=75,
        validators=[
            RegexValidator(r'^[(A-Z)|(a-z)|(\s)|(\-)|(\')]+$', ),
        ],
        blank=True,
        null=True,
    )

    venue = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(r'^[(A-Z)|(a-z)|(\s)|(\-)|(\')]+$', ),
        ],
        blank=True,
        null=True,
    )
    # Job to Shift is a one-to-many relationship
    job = models.ForeignKey(Job)
    # VolunteerShift is the intermediary model
    # for the many-to-many relationship between Volunteer and Shift
    volunteers = models.ManyToManyField(Volunteer, through='VolunteerShift')

    def __str__(self):
        return '{0} - {1}'.format(self.job.name, self.date)
    
class VolunteerShift(models.Model):
    # Volunteer  to VolunteerShift is a one-to-many relationship
    volunteer = models.ForeignKey(Volunteer)
    # Shift to VolunteerShift is a one-to-many relationship
    shift = models.ForeignKey(Shift)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    # assigned_by_manager = models.BooleanField()
    STATUS_CHOICES = (
                     (False,"Not reported"),
                     (True, "Reported"),
                     )
    report_status = models.BooleanField(choices=STATUS_CHOICES,default=False)

    def __str__(self):
        return '{0} - {1}'.format(self.shift, self.volunteer.first_name)

class Report(models.Model):
    total_hrs = models.DecimalField(max_digits=20, decimal_places=4)
    volunteer_shifts = models.ManyToManyField(VolunteerShift)
    # 0: pending 1: confirmed 2: rejected
    confirm_status = models.IntegerField(default=0)
    date_submitted = models.DateField(default=datetime.now().date())

    def get_volunteer(self):
       return self.volunteer_shifts.all()[0].volunteer
    def get_volunteer_shifts(self):
       return self.volunteer_shifts.all()
