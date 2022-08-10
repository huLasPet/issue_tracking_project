#   TODO:
#   6. KB system?
#   7. API calls to get data, option to download data as an Excel file


# Add device to DB:
# device = Devices(users=Users.objects.get(username="asd"), owner="asd", purchase_date=timezone.now(), warranty=timezone.now(), node_id="xyz")
#device.save()
#Search device based on username with users__username    - double _ is to be used to mark relationship in the DB if we need to grab from another model:
#Devices.objects.filter(users__username="ASanyiAkiBela")


