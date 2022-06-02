from django.shortcuts import render, get_object_or_404
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
    tickets = get_object_or_404(Tickets, pk=ticket_id)
    print(request.POST["assigned_user"])
    print(request.POST["affected_user"])
    print(request.POST["assigned_svd"])
    print(request.POST["description"])
    return render(request, 'ticket_app/ticket.html', {'tickets': tickets})

