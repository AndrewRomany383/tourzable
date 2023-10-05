from django.db import models
from django.utils import timezone
from parler.models import TranslatableModel, TranslatedFields
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class Post(TranslatableModel):
    translations = TranslatedFields(
    title=models.CharField(_('title'), max_length=100, blank=True, null=True, db_index=True),
    created_at=models.DateTimeField(_('created_at'), default=timezone.now, db_index=True),
    description=models.TextField(_('description'), max_length=15000, blank=True, null=True, db_index=True),
    slug=models.CharField(_('slug'), max_length=30, unique=True, blank=True, null=True, db_index=True),
    )
    tags=TaggableManager()
    image = models.ImageField(_('image'), upload_to='post/', blank=True, null=True)
    category=models.ForeignKey('Category', related_name='post_category', on_delete=models.CASCADE, verbose_name=_('category'), blank=True, null=True)

    """def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug)
        super(Post, self).save(*args, **kwargs)"""


    def __str__(self):
        return str(self.title)
    def __unicode__(self):
        return self.title





class Category(TranslatableModel):
    translations = TranslatedFields(
    title=models.CharField(_('title'), max_length=50, db_index=True)
    )
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return str(self.title)
    def __unicode__(self):
        return self.title














































