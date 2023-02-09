from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager


# Create your models here.

class User(AbstractBaseUser):
    sex_choices = (("f", "female"), ("m", "male"))
    phone_number = models.CharField(unique=True, max_length=11)
    email = models.EmailField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    sex = models.CharField(max_length=10, choices=sex_choices, default='m')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    age = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"

    REQUIRED_FIELDS = ["email"]  # Just for createsuperuser

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
