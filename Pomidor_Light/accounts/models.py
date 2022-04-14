from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
