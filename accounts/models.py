from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self,username, first_name, last_name, email, remember_me, password=None):
        if email is None:
            raise('Your email is required')
        if username is None:
            raise('Your username is required')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            remember_me=remember_me,
            password=password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, remember_me, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            remember_me=remember_me,
            password=password
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_anonymous = False
        user.is_superadmin = True
        user.is_authenticated = True
        user.is_client = False
        user.is_tour_guide = False
        user.set_password(password)
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    username = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(unique=True, max_length=300, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    profile_image = models.ImageField(upload_to='client_user/', blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    is_tour_guide = models.BooleanField(default=False)
    is_authenticated = True

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'remember_me']
    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True




"""class ClientUserProfile(models.Model):
    user = models.OneToOneField(Account, related_name='client_user', on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    profile_image = models.ImageField(upload_to='client_user/', blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    is_client = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)

class TourGuideUserProfile(models.Model):
    user = models.OneToOneField(Account, related_name='tour_guide_user', on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to='client_user/', blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    is_tour_guide = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)"""



























































