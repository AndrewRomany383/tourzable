from django.contrib import admin
from .models import Property, PropertyImages, Place, Category, PropertyReview, PropertyBook, PropertyAvailabilityCheck, Visa
# Register your models here.

class PropertyImagesAdmin(admin.StackedInline):
    model = PropertyImages

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImagesAdmin,]


admin.site.register(PropertyImages)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyReview)
admin.site.register(PropertyBook)
admin.site.register(PropertyAvailabilityCheck)
admin.site.register(Visa)













