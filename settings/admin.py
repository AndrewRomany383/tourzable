from django.contrib import admin
from .models import Settings
from parler.admin import TranslatableAdmin
# Register your models here.

class SettingsAdmin(TranslatableAdmin):
    list_display = ('site_header',)
    fieldsets = (
        (None, {
            'fields': ('site_header',
                       'phone',
                       'email',
                       'description',
                       'logo',
                       'fb_link',
                       'twitter_link',
                       'instagram_link',
                       'linkedin_link')
        }),
    )

admin.site.register(Settings, SettingsAdmin)






