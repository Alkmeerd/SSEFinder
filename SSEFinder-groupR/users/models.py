from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, primary_key=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    chp_staff_no = models.CharField(max_length=6)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_ad = models.CharField(max_length=500)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username
# Create your models here.


class Case(models.Model):
    case_no = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    id_num = models.CharField(max_length=9, unique=True)
    dob = models.DateField()
    symp_date = models.DateField()
    confirm_date = models.DateField()

    def __str__(self):
        return str(self.case_no)

class Event(models.Model):
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    address = models.CharField(max_length=1000)
    x_coor = models.DecimalField(max_digits=10, decimal_places=3)
    y_coor = models.DecimalField(max_digits=10, decimal_places=3)
    event_date = models.DateField()
    description = models.CharField(max_length=1000)

    case = models.ManyToManyField(Case)

    def __str__(self):
        return (self.name + ", " + self.location + ", " + str(self.event_date))
