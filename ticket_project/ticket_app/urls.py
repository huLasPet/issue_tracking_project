from django.urls import path, include
from . import views

app_name = "ticket_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('all_tickets/<page>', views.all_tickets, name='all_tickets'),
    path('old_tickets', views.old_tickets, name='old_tickets'),
    path('open_new_ticket', views.open_new_ticket, name='open_new_ticket'),
    path('my_open_tickets', views.my_open_tickets, name='my_open_tickets'),
    path('short_warranty', views.short_warranty, name='short_warranty'),
    path('all_devices', views.all_devices, name='all_devices'),
    path('all_users', views.all_users, name='all_users'),
    path('ticket/<ticket_id>', views.ticket, name='ticket'),
    path("search", views.searchresultsview, name="search_results"),
    path("user/<user_id>", views.userview, name="userview"),
    path("device/<node_id>", views.deviceview, name="deviceview"),
]