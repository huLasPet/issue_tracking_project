from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Users, Tickets, Devices
# Create your views here.

def index(request):
    return HttpResponse("Startpage for the issue tracker.")

def test(request):
    users = Users.objects.order_by('id')
    template = loader.get_template('ticket_app/test.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))

def ticket(request):
    tickets = Tickets.objects.order_by('id')
    template = loader.get_template('ticket_app/ticket.html')
    context = {
        'tickets': tickets[0],
    }
    print(tickets[0].users)
    return HttpResponse(template.render(context, request))
