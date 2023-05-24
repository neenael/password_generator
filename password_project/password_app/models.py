from django.db import models


class PasswordData(models.Model):
    length = models.IntegerField()
    mode = models.TextField(null=False, blank=False)
    complexity = models.TextField(null=False, blank=False)