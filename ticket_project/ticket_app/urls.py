from django.urls import path

from . import views

app_name = "ticket_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.all_tickets, name='all_tickets'),
    path('ticket/<ticket_id>', views.ticket, name='ticket')
]