from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    tags = TaggableManager()
    image = models.ImageField(upload_to='post/')
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=15000, blank=True, null=True)
    category = models.ForeignKey('Category', related_name='post_category', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title





class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name














































