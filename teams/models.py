from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"(self.user.username)' s profile"