from django.db import models

# Create your models here.


class Settings(models.Model):
    site_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='settings/')
    phone = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    description = models.TextField(max_length=300)
    fd_link = models.URLField(max_length=300)
    twitter_link = models.URLField(max_length=300)
    instagram_link = models.URLField(max_length=300)
    def __str__(self):
        return self.site_name












































