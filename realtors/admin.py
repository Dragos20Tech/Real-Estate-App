from django.contrib import admin

# Register your models here.

from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)  # registering a Django model called Realtor with the Django admin interface.

# After this registration, you can access and manage instances of the Realtor model through the Django admin panel.

