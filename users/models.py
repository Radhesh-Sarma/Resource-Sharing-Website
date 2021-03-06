from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length = 10)
    address = models.CharField(max_length = 256)
    email = models.EmailField(('email address'), unique=True)
    def __str__(self):
        return self.email

class userdata(models.Model):
    name = models.CharField(max_length = 10)
    email = models.EmailField(('email address'))
    content = models.TextField()
    def __str__(self):
        return self.content

