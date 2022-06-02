from django.urls import path

from . import views

app_name = "ticket_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('ticket/<ticket_id>', views.ticket, name='ticket')
]