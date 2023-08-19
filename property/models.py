from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.db import models
from accounts.models import Account
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name



class Property(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='property/')
    price_of_single_room_by_person = models.PositiveIntegerField(default=0, blank=True, null=True)
    price_of_double_room_by_person = models.PositiveIntegerField(default=0, blank=True, null=True)
    price_of_triple_room_by_person = models.PositiveIntegerField(default=0, blank=True, null=True)
    price_of_single_room_by_night = models.PositiveIntegerField(default=0, blank=True, null=True)
    price_of_double_room_by_night = models.PositiveIntegerField(default=0, blank=True, null=True)
    price_of_triple_room_by_night = models.PositiveIntegerField(default=0, blank=True, null=True)
    description = models.TextField(max_length=10000)
    place = models.ForeignKey('place', related_name='property_place', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.CharField(unique=True, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='property_category', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Properties'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Property, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('property:property_detail', kwargs={'slug':self.slug})



    def check_availability(self):
        all_reservation = self.book_property.all()
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
        all_reviews = self.review_property.all()
        all_rating = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_rating += review.rate
            return round(all_rating/len(all_reviews),2)
        else:
            '-'




class PropertyImages(models.Model):
    property = models.ForeignKey(Property, related_name='property_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return str(self.property)



class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='places/')

    def __str__(self):
        return self.name










class PropertyReview(models.Model):
    auther = models.ForeignKey(Account, related_name='review_auther', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='review_property', on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    feedback = models.TextField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.property)


class PropertyBook(models.Model):
    user = models.ForeignKey(Account, related_name='book_owner', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='book_property', on_delete=models.CASCADE)
    check_in = models.DateField(default=timezone.now)
    check_out = models.DateField(default=timezone.now)
    guest = models.IntegerField(default=0)
    children = models.IntegerField(default=0)

    def __str__(self):
        return str(self.property)

    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    in_progress.boolean = True

class PropertyAvailabilityCheck(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    number_phone = models.CharField(max_length=30, blank=True, null=True)
    Hotel_name = models.CharField(max_length=100)
    check_in = models.DateField(default=timezone.now)
    check_out = models.DateField(default=timezone.now)
    adults_number = models.PositiveIntegerField(default=0)
    children_number = models.PositiveIntegerField(default=0)

    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    in_progress.boolean = True

class Visa(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    visa = models.FileField(upload_to='visas/', blank=True, null=True)
    photo = models.ImageField(upload_to='personal_photos/', blank=True, null=True)






















