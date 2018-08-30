from django.db import models


class User(models.Model):

    name = models.CharField(max_length = 50, null = False)
    password = models.CharField(max_length = 50, null = False)
    status = models.BinaryField(null = False)

class Computer(models.Model):

    name = models.CharField(max_length = 50, null = False)
    ip = models.CharField(max_length = 50, null = False)
    status = models.BinaryField()
    user = models.CharField(max_length = 50, null = True)
    password = models.CharField(max_length = 50, null = True)

class Command(models.Model):

    command = models.CharField(max_length = 300, null = False)
    category = models.CharField(max_length = 150, null = False)
    name = models.CharField(max_length = 50, null = False)