from django.contrib import admin
from .models import Trip, TripGallery, Place, Category, PropertyAvailabilityCheck, Visa, Reservations, Reviews
from parler.admin import TranslatableAdmin
# Register your models here.

class TripGalleryAdmin(admin.StackedInline):
    model = TripGallery

class ReservationAdmin(admin.StackedInline):
    model = Reservations

@admin.register(Trip)
class TripAdmin(TranslatableAdmin):
    inlines = [TripGalleryAdmin,ReservationAdmin]
    list_display = ('title', 'category')
    fieldsets = (
        (None, {
            'fields': ('title',
                       'stars',
                       'image',
                       'price_of_single_room_by_person_night',
                       'price_of_double_room_by_person_night',
                       'price_of_triple_room_by_person_night',
                       'price_of_single_room_by_night',
                       'price_of_double_room_by_night',
                       'price_of_triple_room_by_night',
                       'created_at',
                       'number_of_guests',
                       'number_of_rooms',
                       'duration',
                       'check_in',
                       'check_out',
                       'price_per_child',
                       'description',
                       'place',
                       'slug',
                       'category',
                       'trip_summary',
                       'accommodation',
                       'includes_and_excludes',
                       'itinerary',
                       'cancellation_policy',
                       'terms_conditions',
                       'notes'),
        }),
    )

class PlaceAdmin(TranslatableAdmin):
    list_display = ('title', 'image')
    fieldsets = (
        (None, {
            'fields': ('title', 'image')
        }),
    )

class CategoryAdmin(TranslatableAdmin):
    list_display = ('title',)
    fieldsets = (
        (None, {
            'fields':('title',),
        }),
    )

admin.site.register(TripGallery)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reviews)
admin.site.register(PropertyAvailabilityCheck)
admin.site.register(Visa)
admin.site.register(Reservations)












