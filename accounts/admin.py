from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances


    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["id", "username", "is_admin", "is_superadmin"]
    list_filter = ("is_admin",)
    fieldsets = [
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("username",)}),
        ("Permissions", {"fields": ("is_admin",)}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ("email", "id")
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(Account, UserAdmin)














