from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
# Create your models here.


class Settings(TranslatableModel):
    translations = TranslatedFields(
    site_header=models.CharField(_('site_header'), max_length=50, db_index=True),
    phone=models.CharField(_('phone'), max_length=40, db_index=True),
    email=models.EmailField(_('email'), max_length=100, db_index=True),
    description=models.TextField(_('description'), max_length=300, db_index=True),
    )
    logo = models.ImageField(_('logo'), upload_to='settings/')
    fb_link = models.URLField(_('fb_link'), max_length=300, blank=True, null=True)
    twitter_link = models.URLField(_('twitter_link'), max_length=300, blank=True, null=True)
    instagram_link = models.URLField(_('instagram_link'), max_length=300, blank=True, null=True)
    linkedin_link = models.URLField(_('linkedin_link'), max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.site_header)

    def __unicode__(self):
        return self.site_header












































