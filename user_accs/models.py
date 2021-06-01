from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	SEX_CHOICES = (
		('male', 'Male'),
		('female', 'Female'),
	)
	sex = models.CharField(
		max_length=6,
		choices=SEX_CHOICES,
	)
	date_of_birth = models.DateField(null=True)
	group = models.IntegerField(default=1)
