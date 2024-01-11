from django.contrib import admin

# Register your models here.

from .models import Realtor

admin.site.register(Realtor)  # registering a Django model called Realtor with the Django admin interface.

# After this registration, you can access and manage instances of the Realtor model through the Django admin panel.
