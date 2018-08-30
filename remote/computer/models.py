from django.db import models

class Computer(models.Model):

    name = models.CharField(max_length = 50, null = False)
    ip = models.CharField(max_length = 50, null = False)
    status = models.BinaryField()
    user = models.CharField(max_length = 50, null = True)
    userLogin = models.CharField(max_length = 50, null = True)
    password = models.CharField(max_length = 50, null = True)