from .models import *
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser,Otp
from .forms import UserChangeForm,UserCreationForm


@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    list_display = ["nation_code","otp_code"]
    
    
   

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["full_name", "phone", "adress", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["full_name","phone", ]}),
        ("Personal info", {"fields": ["date_of_birth","adress" ,"national_code", "password"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["full_name", "date_of_birth", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["full_name","date_of_birth","national_code"]
    ordering = ["full_name"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)