from django.db import models

from django.utils.translation import ugettext as _
from redamigos.apps.base.models import BaseModel
from redamigos.apps.enterprise.models import Enterprise

# Create your models here.
class Subsidiary(BaseModel):
    enterprise = models.ForeignKey(
        Enterprise,
        related_name='enterprise'
    )
    town = models.CharField(
        max_length=50,
        null=True
    )
    name = models.CharField(
        max_length=50
    )
    address = models.CharField(
        max_length=50,
        null=True
    )
    picture = models.ImageField(
        upload_to='templates/images/picture/',
        null=True,
        blank=True
    )
    latitude = models.FloatField(
        null=True
    )
    longitude = models.FloatField(
        null=True
    )
    is_active = models.BooleanField(
        _('active'),
        default=True
    )
    user = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return self.name
