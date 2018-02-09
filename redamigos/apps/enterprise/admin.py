from django.contrib import admin

from redamigos.apps.base.admin import BaseAdmin
from redamigos.apps.enterprise.models import Enterprise

# Register your models here.
@admin.register(Enterprise)
class EnterpriseAdmin(BaseAdmin):
    list_display = ('business_name', 'address', 'phone_number',)
