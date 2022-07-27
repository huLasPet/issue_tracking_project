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
    """Index page with cards for displaying some information."""
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
    """Show all curretnly open tickets."""
    tickets = Tickets.objects.filter(state="Open")
    template = loader.get_template('ticket_app/all_tickets.html')
    context = {
        'tickets': tickets,
        'header_text': 'All tickets'
    }
    return HttpResponse(template.render(context, request))


@login_required
def old_tickets(request):
    """Show tickets older than 7 days"""
    older_tickets = Tickets.objects.exclude(opening_date__gt=(datetime.now() - timedelta(days=7)))
    template = loader.get_template('ticket_app/all_tickets.html')
    context = {
        'tickets': older_tickets,
        'header_text': 'Tickets older than 7 days'
    }
    return HttpResponse(template.render(context, request))


@login_required
def my_open_tickets(request):
    """Show the open tickets of the logged in user."""
    my_tickets = Tickets.objects.filter(assigned_user=request.user)
    template = loader.get_template('ticket_app/all_tickets.html')
    context = {
        'tickets': my_tickets,
        'header_text': 'My open tickets'
    }
    return HttpResponse(template.render(context, request))


@login_required
def all_devices(request):
    """Shoe all devices that are not in decomissioned state."""
    devices = Devices.objects.exclude(state="Decomissioned")
    template = loader.get_template('ticket_app/all_devices.html')
    context = {
        'devices': devices,
        'header_text': 'All active devices'
    }
    return HttpResponse(template.render(context, request))


@login_required
def short_warranty(request):
    """Display devices where the warranty is less than 30 days."""
    old_devices = Devices.objects.exclude(warranty__gt=(datetime.now() + timedelta(days=30)))
    template = loader.get_template('ticket_app/all_devices.html')
    context = {
        'devices': old_devices,
        'header_text': 'Devices with less than 30 days of warranty'
    }
    return HttpResponse(template.render(context, request))


@login_required
def all_users(request):
    """Show all non-admin users."""
    #Add pages here, only get the results between 1-10, 11-20 etc based on the pagination from the site.
    #Get "page" after request and use that to only get the needed items from the query
    #Send 100 entries and let the client do the pagination
    users = Users.objects.filter(is_superuser=0, state="Active")#[1:2]
    template = loader.get_template('ticket_app/all_users.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))


@login_required
def open_new_ticket(request):
    """Open a new ticket, users_id is the ID of person who opened the ticket -
     not necessarily the same as the assigned user. This is in order to track who opened the ticket."""
    devices = Devices.objects.exclude(state="Decomissioned")
    users = Users.objects.filter(is_superuser=0)
    svds = []
    for user in users:
        if user.svd not in svds:
            svds.append(user.svd)
    template = loader.get_template('ticket_app/new_ticket.html')
    context = {
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
    """Show search results. Search for exact but not case-sensitive username, nodename, ticket id or
    text in ticket description."""
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
    """Show details for a user and allow updating it."""
    template = loader.get_template('ticket_app/user.html')
    user = Users.objects.filter(id=user_id)[0]
    context = {'users': user}
    if request.method == "POST":
        user.first_name = request.POST["first_name"]
        user.middle_name = request.POST["middle_name"]
        user.title = request.POST["title"]
        user.svd = request.POST["svd"]
        user.state = request.POST["state"]
        user.save()
        return HttpResponseRedirect(f'/user/{user_id}', context)
    return HttpResponse(template.render(context, request))


@login_required
def deviceview(request, node_id):
    """Show details for a device and allow updating it."""
    template = loader.get_template('ticket_app/device.html')
    device = Devices.objects.filter(node_id=node_id)[0]
    state = ["In use", "Warehouse", "Under repair", "Decommissioned"]
    context = {'device': device,
               'state': state}
    if request.method == "POST":
        device.owner = request.POST["owner"]
        device.device_type = request.POST["device_type"]
        device.state = request.POST["state"]
        device.save()
        return HttpResponseRedirect(f'/device/{node_id}', context)
    return HttpResponse(template.render(context, request))



