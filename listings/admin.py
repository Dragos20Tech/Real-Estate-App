from django.contrib import admin

# Register your models here.
# Customize admin stuff for the listing model here.

from .models import Listing

admin.site.register(Listing)
