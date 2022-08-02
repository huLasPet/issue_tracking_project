from datetime import datetime, timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Users(AbstractUser):
    STATE_ACTIVE = 'Active'
    STATE_INACTIVE = 'Inactive'
    STATE_CHOICES = [(STATE_ACTIVE, 'Active'),
                     (STATE_INACTIVE, 'Inactive')]
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default=STATE_ACTIVE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True)
    creation_date = models.DateTimeField('date created', default="1900-01-01")
    username = models.CharField(max_length=200, unique=True)
    svd = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Devices(models.Model):
    STATE_IN_USE = 'In use'
    STATE_DECOMMISSIONED = 'Decommissioned'
    STATE_WH = 'In warehouse'
    STATE_REPAIR = 'Repair'
    STATE_CHOICES = [(STATE_WH, 'Warehouse'),
                     (STATE_REPAIR, 'Repair'),
                     (STATE_DECOMMISSIONED, 'Decommissioned'),
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
    purchase_date = models.DateTimeField('date purchased', default=datetime.now())
    warranty = models.DateTimeField('warranty end', default=(datetime.now() + timedelta(days=3*365)))
    node_id = models.CharField(max_length=50, unique=True)

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
    affected_device = models.CharField(max_length=200, default="")
    opening_date = models.DateTimeField('opening date', default=datetime.now())
    priority = models.CharField(max_length=50, default="Low")

def __int__(self):
        return self.id


class KnowledgeArticles(models.Model):
    STATE_ACTIVE = 'Active'
    STATE_INACTIVE = 'Inactive'
    STATE_CHOICES = [(STATE_ACTIVE, 'Active'),
                 (STATE_INACTIVE, 'Inactive')]
    description = models.CharField(max_length=100000)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default=STATE_ACTIVE)
    creation_date = models.DateTimeField('Creation date', default=datetime.now())
    created_by = models.CharField(max_length=200)
    modified_by = models.CharField(max_length=200)

def __int__(self):
    return self.id
