from django.db import models

class Command(models.Model):

    command = models.CharField(max_length = 300, null = False)
    category = models.CharField(max_length = 150, null = False)
    name = models.CharField(max_length = 50, null = False)
    report = models.IntegerField(null = False)
