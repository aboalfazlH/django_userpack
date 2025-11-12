from django.db import models
from django.contrib.auth.models import AbstractUser

class AdvancedUser(AbstractUser):
    # Auth fields
    phone_number = models.CharField()
    national_code = models.CharField()


    
    # Personal information
    
    ## times and numbers
    
    birth_day = models.DateTimeField()
    verify_date = models.DateTimeField()
    age = models.PositiveSmallIntegerField()

    ## permissions
    is_verify = models.BooleanField()

    ## more
    bio = models.TextField()
    avatar = models.ImageField()