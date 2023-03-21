from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email_address'), unique=True)    
    phone = models.CharField(_("phone"), max_length=50, blank=True, null=True)
    address = models.TextField()
    company = models.CharField(_("company"), max_length=200, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    def __str__(self) -> str:
        return self.email
    