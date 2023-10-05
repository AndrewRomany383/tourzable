from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import About, FAQ, ContactUs, ContactConsultant

# Register your models here.

class AboutAdmin(TranslatableAdmin):
    list_display = ('who_we_are', 'what_we_do', 'our_mission', 'our_goals')
    fieldsets = (
        (None, {
            'fields': ('who_we_are', 'what_we_do', 'our_mission', 'our_goals'),
        }),
    )

class FAQAdmin(TranslatableAdmin):
    list_display = ('question', 'answer')
    fieldsets = (
        (None, {
            'fields': ('question', 'answer'),
        }),
    )

admin.site.register(About, AboutAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(ContactUs)
admin.site.register(ContactConsultant)















