from django.db import models
from django.contrib.auth.models import AbstractUser

class AdvancedUser(AbstractUser):
    phone_number = models.CharField()
    national_code = models.CharField()
    