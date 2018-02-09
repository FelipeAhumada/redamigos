from django.db import models

from redamigos.apps.base.models import BaseModel
from redamigos.apps.subsidiary.models import Subsidiary

# Create your models here.
class Type(BaseModel):
    description = models.CharField(
        max_length=100,
    )


class Delivery(BaseModel):
    quantity = models.SmallIntegerField(
        default=0,
    )
    photo = models.ImageField(
        upload_to='templates/images/photo/',
        null=True,
        blank=True
    )
    subsidiary = models.ForeignKey(
        Subsidiary,
        related_name='delivery_subsidiary'
    )
    type = models.ForeignKey(
        Type,
        related_name='delivery_type'
    )
