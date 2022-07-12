from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Users, Tickets, Devices, KnowledgeArticles
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.db.models import Q


# Create your views here.

# REMOVE DUPLICATES WHEN ALL VIEWS ARE DONE


@login_required
def index(request):
    open_tickets_count = Tickets.objects.filter(state='Open').count()
    older_tickets_count = Tickets.objects.exclude(opening_date__gt=(datetime.now() - timedelta(days=7))).count()
    old_devices_count = Devices.objects.exclude(warranty__gt=(datetime.now() + timedelta(days=30))).count()
    my_tickets_count = Tickets.objects.filter(assigned_user=request.user).count()
    kb_count = KnowledgeArticles.objects.filter(state='Active').count()
    template = loader.get_template('ticket_app/index.html')
    context = {
        'open_tickets_count': open_tickets_count,
        'older_tickets_count': older_tickets_count,
        'old_devices_count': old_devices_count,
        'my_tickets_count': my_tickets_count,
        'kb_count': kb_count,
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
    """Display devices where the warranty is less than 30 days."""
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
def open_new_ticket(request):
    """Open a new ticket, users_id is the ID of person who opened the ticket -
     not necessarily the same as the assigned user. This is in order to track who opened the ticket."""
    tickets = Tickets.objects.all()
    devices = Devices.objects.all()
    users = Users.objects.filter(is_superuser=0)
    svds = []
    for user in users:
        if user.svd not in svds:
            svds.append(user.svd)
    template = loader.get_template('ticket_app/new_ticket.html')
    context = {
        'tickets': tickets,
        'devices': devices,
        'users': users,
        'svds': svds
    }
    if request.method == "POST":
        user = Users.objects.filter(username=request.user)
        new_ticket = Tickets(affected_user=request.POST["affected_user"],
                             affected_device=request.POST["affected_device"],
                             assigned_user=request.POST["assigned_user"],
                             assigned_svd=request.POST["assigned_svd"],
                             description=request.POST["description"],
                             state=request.POST["state"],
                             users_id=user[0].id)

        new_ticket.save()
        return HttpResponseRedirect("/")
    return HttpResponse(template.render(context, request))


@login_required
def ticket(request, ticket_id):
    # Try to add action history, one big string with something static to separate actions and use regex to list them
    # separately later
    """Open ticket where ticket_id is the Ticket.id from the DB,
    devices are the affected user's devices if there are any, No device otherwise,
    svds are the all the SVDs without duplicates.
    Get data back to update the DB, refresh the page."""
    ticket_id = int(ticket_id)
    tickets = get_object_or_404(Tickets, pk=ticket_id)
    devices = Devices.objects.filter(users__username=tickets.affected_user)
    if not devices:
        devices = ["No device"]
    users = Users.objects.filter(is_superuser=0)
    svds = []
    template = loader.get_template('ticket_app/ticket.html')
    for user in users:
        if user.svd not in svds:
            svds.append(user.svd)
    context = {'tickets': tickets,
               'devices': devices,
               'users': users,
               'svds': svds}
    if request.method == "POST":
        tickets.affected_user = request.POST["affected_user"]
        tickets.affected_device = request.POST["affected_device"]
        tickets.assigned_user = request.POST["assigned_user"]
        tickets.assigned_svd = request.POST["assigned_svd"]
        tickets.description = request.POST["description"]
        tickets.state = request.POST["state"]
        tickets.save()
        return HttpResponseRedirect(f'/ticket/{ticket_id}', context)
    return HttpResponse(template.render(context, request))


@login_required
def searchresultsview(request):
    search_term = request.POST["search"]
    template = loader.get_template('ticket_app/search.html')
    user_search = Users.objects.filter(username__iexact=search_term)
    ticket_search = Tickets.objects.filter(Q(id__iexact=search_term) | Q(description__icontains=search_term))
    device_search = Devices.objects.filter(node_id__iexact=search_term)
    kb_search = KnowledgeArticles.objects.filter(description__icontains=search_term)
    context = {'search_term': search_term,
               'users_search': user_search,
               'ticket_search': ticket_search,
               'device_search': device_search,
               'kb_search': kb_search}
    return HttpResponse(template.render(context, request))

@login_required
def userview(request, user_id):
    template = loader.get_template('ticket_app/user.html')
    user = Users.objects.filter(id=user_id)
    context = {'user': user[0]}
    return HttpResponse(template.render(context, request))


@login_required
def deviceview(request, node_id):
    template = loader.get_template('ticket_app/device.html')
    device = Devices.objects.filter(node_id=node_id)
    context = {'device': device[0]}
    return HttpResponse(template.render(context, request))



