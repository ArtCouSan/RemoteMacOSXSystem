from django.db import models

class Report(models.Model):

    command = models.CharField(max_length = 300, null = False)
    condition = models.CharField(max_length = 150, null = False)
    name = models.CharField(max_length = 50, null = False)
