from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    chp_staff_no = models.DecimalField(max_digits=6, decimal_places=0)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_ad = models.CharField(max_length=500)
    
    def __str__(self):
        return self.username