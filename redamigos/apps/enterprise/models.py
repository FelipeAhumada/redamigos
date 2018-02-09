from django.db import models

from django.utils.translation import ugettext as _
from redamigos.apps.base.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Enterprise(BaseModel):
    address = models.CharField(
        max_length=50,
        blank=True
    )
    phone_number = PhoneNumberField(
        blank=True
    )
    logotype = models.ImageField(
        upload_to='templates/images/logo/',
        blank=True
    )
    business_name = models.CharField(
        max_length=70
    )
    commercial_business = models.CharField(
        max_length=150,
        blank=True
    )
    rut = models.CharField(
        max_length=9,
        unique=True
    )
    is_active = models.BooleanField(
        _('active'),
        default=True
    )

    def __str__(self):
        return self.commercial_business
