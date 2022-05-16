import random

from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')
    username = models.CharField(max_length=200, unique=True)
    svd = models.CharField(max_length=200)
    title = models.CharField(max_length=200)


class Devices(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    owner = models.CharField(max_length=200)
    device_type = models.CharField(max_length=200)
    state = models.CharField(max_length=30, default='In warehouse')
    purchase_date = models.DateTimeField('date purchased')
    warranty = models.DateTimeField('warranty end')


class Tickets(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    affected_user = models.CharField(max_length=200)
    assigned_user = models.CharField(max_length=200)
    assigned_svd = models.CharField(max_length=200)
    ticket_number = models.IntegerField(default=random.randint(1, 100), unique=True)
    state = models.CharField(max_length=20, default='Open')
    description = models.CharField(max_length=1000)



