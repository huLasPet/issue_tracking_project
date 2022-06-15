from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Users, Tickets, Devices
# Create your views here.


def index(request):
    return render(request, 'ticket_app/index.html')


def all_tickets(request):
    tickets = Tickets.objects.order_by('id')
    template = loader.get_template('ticket_app/all.html')
    context = {
        'tickets': tickets,
    }
    return HttpResponse(template.render(context, request))


def ticket(request, ticket_id):
    """Open ticket where ticket_id is the Ticket.id from the DB
    Get data back to update the DB, refresh the page."""
    ticket_id = int(ticket_id)
    tickets = get_object_or_404(Tickets, pk=ticket_id)
    devices = Devices.objects.filter(users__username=tickets.affected_user)
    users = Users.objects.order_by('username')
    if request.method == "POST":
        tickets.affected_user = request.POST["affected_user"]
        tickets.affected_device = request.POST["affected_device"]
        tickets.assigned_user = request.POST["assigned_user"]
        tickets.assigned_svd = request.POST["assigned_svd"]
        tickets.description = request.POST["description"]
        tickets.state = request.POST["state"]
        tickets.save()
        return HttpResponseRedirect(f'/ticket/{ticket_id}', {'tickets': tickets, 'devices': devices, 'users': users})
    return render(request, 'ticket_app/ticket.html', {'tickets': tickets, 'devices': devices, 'users': users})

