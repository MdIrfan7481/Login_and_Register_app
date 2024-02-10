from django.db import models

# Create your models here.
class Reg(models.Model):
    FirstName = models.CharField(max_length=10)
    LastName = models.CharField(max_length=10)
    UserName = models.CharField(max_length=10)
    Password = models.CharField(max_length=10)
    Cpassword= models.CharField(max_length=10)
    MobileNumber = models.IntegerField()
    EmailId = models.EmailField()
