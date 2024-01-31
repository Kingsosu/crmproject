from django.db import models
from django.conf import settings
from account.models import Account

# Create your models here.

class Record(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=255)
    lga = models.CharField(max_length=255)
    country = models.CharField(max_length=125)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.first_name + " " + self.last_name + " | " + self.email

