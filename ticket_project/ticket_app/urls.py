from django.urls import path, include

from . import views

app_name = "ticket_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('all_tickets', views.all_tickets, name='all_tickets'),
    path('all_devices', views.all_devices, name='all_devices'),
    path('all_users', views.all_users, name='all_users'),
    path('ticket/<ticket_id>', views.ticket, name='ticket')
]