#   TODO:
#   1.Auth system - auth0 or maybe built-in django one?
#   2. DB for tickets, users, devices
#       2.a: Users: 1st name, last name, middle name, username, department, point to tickets and devices
#       2.b: Tickets: ticket number, description, state, assigned SVD and user, affected user, item
#       2.c: Devices: device type, owner, start use, warranty end, state (in use, loaner, in warehouse)
#   3. Show tickets assigned to me and my team
#   4. Different pages for showing all tickets, handling tickets/users/devices
#   5. Filtering tickets
#   6. KB system?


# Add device to DB:
# device = Devices(users=Users.objects.get(username="asd"), owner="asd", purchase_date=timezone.now(), warranty=timezone.now(), node_id="xyz")
#device.save()
#Search device based on username with users__username    - double _ is to be used to mark relationship in the DB if we need to grab from another model:
#Devices.objects.filter(users__username="ASanyiAkiBela")





