from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    chp_staff_no = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_ad = models.CharField(max_length=500)

    def __str__(self):
        return self.username

class Case(models.Model):
    case_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    id_num = models.CharField(max_length=9, unique = True)
    dob = models.DateField()
    symp_date = models.DateField()
    confirm_date = models.DateField()

    def __str__(self):
        return self.case_no

class Event(models.Model):
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    address = models.CharField(max_length=1000)
    x_coor = models.DecimalField(max_digits=10, decimal_places=3)
    y_coor = models.DecimalField(max_digits=10, decimal_places=3)
    event_date = models.DateField()
    description = models.CharField(max_length=1000)

    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    def __str__(self):
        return self.name