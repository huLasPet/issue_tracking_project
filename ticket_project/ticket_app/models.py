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

    def __str__(self):
        return self.username


class Devices(models.Model):
    STATE_IN_USE = 'In use'
    STATE_DECOMISSIONED = 'Decomissioned'
    STATE_WH = 'In warehouse'
    STATE_REPAIR = 'Under repair'
    STATE_CHOICES = [(STATE_WH, 'Warehouse'),
                     (STATE_REPAIR, 'Repair'),
                     (STATE_DECOMISSIONED, 'Decomissioned'),
                     (STATE_IN_USE, 'In use')]
    TYPE_LAPTOP = "Laptop"
    TYPE_DESKTOP = "Desktop"
    TYPE_VM = "Virtual"
    TYPE_CHOICE = [(TYPE_VM, "Virtual"),
                   (TYPE_DESKTOP, "Desktop"),
                   (TYPE_LAPTOP, "Laptop")]
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    owner = models.CharField(max_length=200)
    device_type = models.CharField(max_length=200, choices=TYPE_CHOICE)
    state = models.CharField(max_length=30, choices=STATE_CHOICES, default=STATE_WH)
    purchase_date = models.DateTimeField('date purchased')
    warranty = models.DateTimeField('warranty end')
    node_id = models.CharField(max_length=50, unique=True, default='None')

    def __str__(self):
        return self.node_id


class Tickets(models.Model):
    STATE_OPEN = 'Open'
    STATE_CLOSED = 'Closed'
    STATE_CHOICES = [(STATE_OPEN, 'Open'),
                     (STATE_CLOSED, 'Closed')]
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    affected_user = models.CharField(max_length=200)
    assigned_user = models.CharField(max_length=200)
    assigned_svd = models.CharField(max_length=200)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default=STATE_OPEN)
    description = models.CharField(max_length=100000)

    def __int__(self):
        return self.id
