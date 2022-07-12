from django.contrib import admin
from .models import Users, Devices, Tickets, KnowledgeArticles
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Users
    list_display = ["username"]
    fieldsets = tuple(
        (fieldset[0], {
            **{key: value for (key, value) in fieldset[1].items() if key != 'fields'},
            'fields': fieldset[1]['fields'] + ('middle_name', 'svd', 'title')
        })
        if fieldset[0] == 'Personal info'
        else fieldset
        for fieldset in UserAdmin.fieldsets
    )


admin.site.register(Users, CustomUserAdmin)
admin.site.register(Devices)
admin.site.register(Tickets)
admin.site.register(KnowledgeArticles)