from django.contrib import admin

from redamigos.apps.base.admin import BaseAdmin
from redamigos.apps.subsidiary.models import Subsidiary

# Register your models here.
@admin.register(Subsidiary)
class SubsidiaryAdmin(BaseAdmin):
    list_display = ('enterprise', 'name', 'address')
