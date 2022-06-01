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

def ticket(request, ticket_id):
    """Open ticket where ticket_id is the Ticket.id from the DB"""
    ticket_id = int(ticket_id)
    tickets = Tickets.objects.get(pk=ticket_id)
    template = loader.get_template('ticket_app/ticket.html')
    context = {
        'tickets': tickets,
    }
    return HttpResponse(template.render(context, request))
