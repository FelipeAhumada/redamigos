from django.contrib import admin

from redamigos.apps.base.admin import BaseAdmin
from redamigos.apps.chip.models import Chip

# Register your models here.
@admin.register(Chip)
class ChipAdmin(BaseAdmin):
    list_display = ('lccid',)
