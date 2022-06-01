from django.shortcuts import render
from django.http import HttpResponse
from .models import Users, Tickets, Devices
# Create your views here.

def index(request):
    return HttpResponse("Startpage for the issue tracker.")

def test(request):
    users = Users.objects.order_by('id')
    output = ', '.join([user.username for user in users])
    ticket = Tickets.objects.filter(affected_user="asd")
    return HttpResponse("Users: %s" % output + "  ||| Ticket #: %s" % ticket[0].affected_user)
