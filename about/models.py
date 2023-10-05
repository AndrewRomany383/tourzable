from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
# Create your models here.

class About(TranslatableModel):
    translations = TranslatedFields(
    who_we_are=models.TextField(_('who_we_are'), max_length=1000, db_index=True),
    what_we_do=models.TextField(_('what_we_do'), max_length=1000, db_index=True),
    our_mission=models.TextField(_('our_mission'), max_length=1000, db_index=True),
    our_goals=models.TextField(_('our_goals'), max_length=1000, db_index=True),
    )

    def __str__(self):
        return str(self.who_we_are)

    def __unicode__(self):
        return self.who_we_are


class FAQ(TranslatableModel):
    translations = TranslatedFields(
    question=models.CharField(_('question'), max_length=150, blank=False, null=True, db_index=True),
    answer=models.TextField(_('answer'), max_length=3000, blank=False, null=True, db_index=True),
    )
    def __str__(self):
        return str(self.title)

    def __unicode__(self):
        return self.title

class ContactUs(models.Model):
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

    def __str__(self):
        return self.firstname
class ContactConsultant(models.Model):
    firstname = models.CharField(_('firstname'), max_length=50, blank=True, null=True)
    lastname = models.CharField(_('lastname'), max_length=50, blank=True, null=True)
    email = models.EmailField(_('email'), blank=True, null=True)
    number_phone = models.CharField(_('number_phone'), max_length=30, blank=True, null=True)
    place = models.CharField(_('place'), max_length=100, blank=True, null=True)
    check_in = models.DateField(_('check_in'), default=timezone.now)
    check_out = models.DateField(_('check_out'), default=timezone.now)
    adults_number = models.PositiveIntegerField(_('adults_number'), default=0, blank=True, null=True)
    children_number_and_their_age = models.TextField(_('children_number_and_their_age'), max_length=1000, blank=True, null=True)
    infant = models.CharField(_('infant'), max_length=1000, blank=True, null=True)
    room_number = models.PositiveIntegerField(_('room_number'), default=0, blank=True, null=True)
    notes = models.TextField(_('notes'), max_length=1000, blank=True, null=True)
    consultant_request = models.CharField(_('consultant_request'), default=True)

    def __str__(self):
        return self.firstname

































