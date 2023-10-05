from django import forms
from django.contrib import admin
from .models import Account
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = '__all__'

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don"t match')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = '__all__'

        def clean_password(self):
            return self.initial["password"]




class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    model = Account
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["username", "is_admin", "is_superuser"]
    list_filter = ("is_admin",)
    fieldsets = [
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("username", "first_name",
                                      "last_name", "phone_number",
                                      "profile_image", "language")}),
        ("Permissions", {"fields": ("is_admin", "is_active",
                                    "is_staff","is_superuser", "groups", "user_permissions",)}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ('email', 'username', 'password1', 'password2')
            },
        ),
    ]
    search_fields = ["email", "username"]
    ordering = ("email", "id")
    filter_horizontal = ("groups", "user_permissions")

# Now register the new UserAdmin...
admin.site.register(Account, CustomUserAdmin)













