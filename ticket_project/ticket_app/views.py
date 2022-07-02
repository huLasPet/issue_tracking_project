from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from .models import Users, Tickets, Devices
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta


# Create your views here.


@login_required
def index(request):
    open_tickets_count = Tickets.objects.filter(state='Open').count()
    older_tickets_count = Tickets.objects.exclude(opening_date__gt=(datetime.now() - timedelta(days=7))).count()
    old_devices_count = Devices.objects.exclude(warranty__gt=(datetime.now() + timedelta(days=30))).count()
    my_tickets_count = Tickets.objects.filter(assigned_user=request.user).count()
    template = loader.get_template('ticket_app/index.html')
    context = {
        'open_tickets_count': open_tickets_count,
        'older_tickets_count': older_tickets_count,
        'old_devices_count': old_devices_count,
        'my_tickets_count': my_tickets_count,
    }
    return HttpResponse(template.render(context, request))


@login_required
def all_tickets(request):
    tickets = Tickets.objects.order_by('id')
    template = loader.get_template('ticket_app/all_tickets.html')
    context = {
        'tickets': tickets,
    }
    return HttpResponse(template.render(context, request))


@login_required
def old_tickets(request):
    """Show tickets older than 7 days"""
    older_tickets = Tickets.objects.exclude(opening_date__gt=(datetime.now() - timedelta(days=7)))
    template = loader.get_template('ticket_app/all_tickets.html')
    context = {
        'tickets': older_tickets,
    }
    return HttpResponse(template.render(context, request))


@login_required
def open_new_ticket(request):
    pass


@login_required
def my_open_tickets(request):
    my_tickets = Tickets.objects.filter(assigned_user=request.user)
    template = loader.get_template('ticket_app/all_tickets.html')
    context = {
    'tickets': my_tickets,
    }
    return HttpResponse(template.render(context, request))



@login_required
def all_devices(request):
    devices = Devices.objects.order_by('id')
    template = loader.get_template('ticket_app/all_devices.html')
    context = {
        'devices': devices,
    }
    return HttpResponse(template.render(context, request))


@login_required
def short_warranty(request):
    old_devices = Devices.objects.exclude(warranty__gt=(datetime.now() + timedelta(days=30)))
    template = loader.get_template('ticket_app/all_devices.html')
    context = {
        'devices': old_devices,
    }
    return HttpResponse(template.render(context, request))


@login_required
def all_users(request):
    users = Users.objects.filter(is_superuser=0)
    template = loader.get_template('ticket_app/all_users.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))


@login_required
def ticket(request, ticket_id):
    # Try to add action history, one big string with something static to separate actions and use regex to list them
    # separately later
    """Open ticket where ticket_id is the Ticket.id from the DB
    Get data back to update the DB, refresh the page."""
    ticket_id = int(ticket_id)
    tickets = get_object_or_404(Tickets, pk=ticket_id)
    devices = Devices.objects.filter(users__username=tickets.affected_user)
    users = Users.objects.filter(is_superuser=0)
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
