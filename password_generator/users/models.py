from django.db import models
from django.contrib.auth.models import User

class PasswordModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=30)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user} - {self.platform}'

