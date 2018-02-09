from django.db import models

from redamigos.apps.base.models import BaseModel
from redamigos.apps.deliveries.models import Delivery


# Create your models here.
class State(BaseModel):
    description = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.description


class Chip(BaseModel):
    lccid = models.CharField(
        max_length=20
    )
    text = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    user = models.CharField(
        max_length=150,
    )
    state = models.ForeignKey(
        State,
        related_name='chip_status',
        null=True
    )

    def __str__(self):
        return self.lccid


class ChipDelivery(BaseModel):
    chip = models.OneToOneField(
        Chip,
        related_name='chip_sale',
        null=True
    )
    delivery = models.ForeignKey(
        Delivery,
        related_name='delivery_sale',
        null=True
    )
