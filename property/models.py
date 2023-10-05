from django.utils import timezone
from parler.models import TranslatableModel, TranslatedFields
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db import models
from accounts.models import Account
# Create your models here.


class Category(TranslatableModel):
    translations = TranslatedFields(
    title=models.CharField(_('title'), max_length=40, db_index=True)
    )
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return str(self.title)
    def __unicode__(self):
        return self.title



class Trip(TranslatableModel):
    translations = TranslatedFields(
    title=models.CharField(_('title'), max_length=100, db_index=True),
    description=models.TextField(_('description'), max_length=10000, db_index=True),
    slug=models.CharField(_('slug'), unique=True, blank=True, null=True, db_index=True),
    trip_summary=models.CharField(_('trip_summary'), max_length=100, blank=True, null=True, db_index=True),
    accommodation=models.CharField(_('accommodation'), max_length=20, blank=True, null=True, db_index=True),
    includes_and_excludes=models.CharField(_('includes_and_excludes'), max_length=200, blank=True, null=True, db_index=True),
    itinerary=models.CharField(_('itinerary'), max_length=200, blank=True, null=True, db_index=True),
    cancellation_policy=models.CharField(_('cancellation_policy'), max_length=200, blank=True, null=True, db_index=True),
    terms_conditions=models.CharField(_('terms_conditions'), max_length=200, blank=True, null=True, db_index=True),
    notes=models.CharField(_('notes'), max_length=200, blank=True, null=True, db_index=True)
    )
    stars = models.CharField(_('stars'), max_length=20, blank=True, null=True)
    price_of_single_room_by_person_night = models.PositiveIntegerField(_('price_of_single_room_by_person_night'),
                                                                       default=0, blank=True, null=True)
    price_of_double_room_by_person_night = models.PositiveIntegerField(_('price_of_double_room_by_person_night'),
                                                                       default=0, blank=True, null=True)
    price_of_triple_room_by_person_night = models.PositiveIntegerField(_('price_of_triple_room_by_person_night'),
                                                                       default=0, blank=True, null=True)
    price_of_single_room_by_night = models.PositiveIntegerField(_('price_of_single_room_by_night'), default=0,
                                                                blank=True, null=True)
    price_of_double_room_by_night = models.PositiveIntegerField(_('price_of_double_room_by_night'), default=0,
                                                                blank=True, null=True)
    price_of_triple_room_by_night = models.PositiveIntegerField(_('price_of_triple_room_by_night'), default=0,
                                                                blank=True, null=True)
    image = models.ImageField(_('image'), upload_to='property/')
    place=models.ForeignKey('Place', related_name='property_place', on_delete=models.CASCADE, verbose_name=_('place'))
    category=models.ForeignKey(Category, related_name='property_category', on_delete=models.CASCADE, verbose_name=_('category'))
    created_at = models.DateTimeField(_('created_at'), default=timezone.now)
    number_of_guests = models.PositiveIntegerField(_('number_of_guests'), default=0, blank=True, null=True)
    number_of_rooms = models.PositiveIntegerField(_('number_of_rooms'), default=0, blank=True, null=True)
    duration = models.PositiveIntegerField(_('duration'), default=0, blank=True, null=True)
    price_per_child = models.PositiveIntegerField(_('price_per_child'), default=0, blank=True, null=True)
    check_in = models.DateField(_('check_in'),blank=False , null=True)
    check_out = models.DateField(_('check_out'),blank=False , null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Trip, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('property:property_detail', kwargs={'slug':self.slug})



    def check_availability(self):
        all_reservation = self.book_trip.all()
        now = timezone.now().date()
        for reservation in all_reservation:
            if now > reservation.check_out:
                return 'reservation has been finished'
            elif now > reservation.check_out and now < reservation.check_in:
                reserved_to = reservation.check_out
                return f'In progress {reserved_to}'
        else:
            return 'available'




    def get_avg_rating(self):
        all_reviews = self.review_trip.all()
        all_rating = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_rating += review.rate
            return round(all_rating/len(all_reviews),2)
        else:
            '-'




class TripGallery(models.Model):
    trip = models.ForeignKey(Trip, related_name='TripGallery_images', on_delete=models.CASCADE, verbose_name=_('trip'))
    image = models.ImageField(_('image'), upload_to='trip_images/')

    def __str__(self):
        return str(self.trip)



class Place(TranslatableModel):
    translations = TranslatedFields(
    title=models.CharField(_('title'), max_length=50, db_index=True)
    )
    image = models.ImageField(_('image'), upload_to='places/')
    def __str__(self):
        return str(self.title)

    def __unicode__(self):
        return self.title


class PropertyAvailabilityCheck(models.Model):
    firstname = models.CharField(_('firstname'), max_length=50, blank=True, null=True)
    lastname = models.CharField(_('lastname'), max_length=50, blank=True, null=True)
    email = models.EmailField(_('email'), blank=True, null=True)
    number_phone = models.CharField(_('number_phone'), max_length=30, blank=True, null=True)
    place = models.CharField(_('place'), max_length=100, blank=True, null=True)
    check_in = models.DateField(_('check_in'), default=timezone.now)
    check_out = models.DateField(_('check_out'), default=timezone.now)
    adults_number = models.PositiveIntegerField(_('adults_number'), default=0, blank=True, null=True)
    children_number_and_their_age = models.TextField(_('children_number_and_their_age'), max_length=1000, blank=True, null=True)
    infant = models.TextField(_('infant'), max_length=1000, blank=True, null=True)
    room_number = models.PositiveIntegerField(_('room_number'), default=0, blank=True, null=True)
    notes = models.TextField(_('notes'), max_length=1000, blank=True, null=True)
    user = models.ForeignKey(Account, related_name='inquiry_owner',on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('user'))

    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    in_progress.boolean = True

class Visa(models.Model):
    user = models.ForeignKey(Account, related_name='visa_owner', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('user'))
    email = models.EmailField(_('email'), blank=True, null=True)
    number_phone = models.CharField(_('number_phone'), max_length=30, blank=True, null=True)
    visa = models.FileField(_('visa'), upload_to='visas/', blank=True, null=True)
    photo = models.ImageField(_('photo'), upload_to='personal_photos/', blank=True, null=True)
    def __str__(self):
        return self.email



class Reservations(models.Model):
    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    client = models.ForeignKey(Account, related_name="client_reservations", on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, related_name="client_trips", on_delete=models.CASCADE)
    adult_number = models.PositiveIntegerField(default=0, null=True)
    guests_info = models.TextField(max_length=10000, null=True)
    children_number_and_their_age = models.TextField(max_length=10000, null=True)
    infant = models.PositiveIntegerField(default=0, null=True)
    notes = models.TextField(max_length=10000, null=True)
    created_at = models.DateTimeField(default=timezone.now)


    class Meta:
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return f"{self.client} - {self.trip} - {self.status} - {self.created_at}"

    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    in_progress.boolean = True

class Reviews(models.Model):
    client = models.ForeignKey(Account, related_name="client_reviews", on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, related_name="client_reviews", on_delete=models.CASCADE, null=True)
    rate = models.FloatField(default=0, null=True)
    feedback = models.TextField(max_length=10000, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.client} - {self.trip} - {self.rate} - {self.created_at}"



class Favorites(models.Model):
    client = models.ForeignKey(Account, related_name="client_favorites", on_delete=models.CASCADE)
    favs = models.ForeignKey(Trip, related_name="trip_favorites", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Favorites'

    def __str__(self):
        return f"{self.client} - {self.favs} - {self.created_at}"











