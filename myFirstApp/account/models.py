from django.contrib.auth.models import User
from django.db import models


class UserActivity(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_login = models.DateTimeField()
