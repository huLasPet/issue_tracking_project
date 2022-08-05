#   TODO:
#   6. KB system?
#   7. API calls to get data, option to download data as an Excel file
#   8. Add some sort of background <div> with a light grey color to the forms


# Add device to DB:
# device = Devices(users=Users.objects.get(username="asd"), owner="asd", purchase_date=timezone.now(), warranty=timezone.now(), node_id="xyz")
#device.save()
#Search device based on username with users__username    - double _ is to be used to mark relationship in the DB if we need to grab from another model:
#Devices.objects.filter(users__username="ASanyiAkiBela")



#Regex: https://stackoverflow.com/questions/9889635/regular-expression-to-return-all-characters-between-two-special-characters
import re
pat = r'(?<=\[).+?(?=\])'
s = r"0000[sometexthere]0000[somemoretextheretoo]"
match_object = re.findall(pat, s)
for object in match_object:
    print(object)

