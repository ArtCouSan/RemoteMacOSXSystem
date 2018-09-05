from django.db import models

class Result(models.Model):

    result = models.CharField(max_length = 200)
