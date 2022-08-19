#   TODO:
#   6. KB system?
#   9. Instead of many API functions, have only 1 that gets all its data from the <> in the address -
#       like <all_ticket> for all tickets or <one_ticket>/<ticket_number> for just one
#       https://stackoverflow.com/questions/14351048/django-optional-url-parameters
#   10. Add option to filter tables on the site


# Add device to DB:
# device = Devices(users=Users.objects.get(username="asd"), owner="asd", purchase_date=timezone.now(), warranty=timezone.now(), node_id="xyz")
#device.save()
#Search device based on username with users__username    - double _ is to be used to mark relationship in the DB if we need to grab from another model:
#Devices.objects.filter(users__username="ASanyiAkiBela")


