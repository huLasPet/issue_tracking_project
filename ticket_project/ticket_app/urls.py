from django.urls import path
from . import views

app_name = "ticket_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('all_tickets', views.all_tickets, name='all_tickets'),
    path('old_tickets', views.old_tickets, name='old_tickets'),
    path('open_new_ticket', views.open_new_ticket, name='open_new_ticket'),
    path('my_open_tickets', views.my_open_tickets, name='my_open_tickets'),
    path('short_warranty', views.short_warranty, name='short_warranty'),
    path('all_devices/', views.all_devices, name='all_devices'),
    path('all_users/', views.all_users, name='all_users'),
    path('ticket/<ticket_id>', views.ticket, name='ticket'),
    path("search/<search_term>", views.searchresultsview, name="search_results"),
    path("user/<user_id>", views.userview, name="userview"),
    path("device/<node_id>", views.deviceview, name="deviceview"),
    path('all_users/api-all', views.api_get_all_users, name='api_all_users'),
    path(r'all_users/api-one', views.api_get_one_user, name='api_one_user'),
    path('all_devices/api-all', views.api_get_all_devices, name='api_all_devices'),
    path('all_devices/api-one', views.api_get_one_device, name='api_one_device'),
    path('all_tickets/api-all', views.api_get_all_tickets, name='api_all_tickets'),
    path('all_tickets/api-one', views.api_get_one_ticket, name='api_one_ticket'),
    path('all_kbs/api-all', views.api_get_all_kbs, name='api_all_kbs'),
    path('all_kbs/api-one', views.api_get_one_kb, name='api_one_kb'),
    path('all_users_xlsx', views.all_users_xlsx, name='all_users_xlsx'),
    path('all_devices_xlsx', views.all_devices_xlsx, name='all_devices_xlsx'),
    path('all_tickets_xlsx', views.all_tickets_xlsx, name='all_tickets_xlsx'),
    path('api', views.api_view, name='api_view'),



]