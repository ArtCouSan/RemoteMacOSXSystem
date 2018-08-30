from django.db import models


class User(models.Model):

    name = models.CharField(max_length = 50, null = False)
    password = models.CharField(max_length = 50, null = False)
    status = models.BinaryField(null = False)



