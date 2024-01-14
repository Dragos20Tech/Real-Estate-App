from django.contrib import admin

# Register your models here.
# Customize admin stuff for the listing model here.

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')  # Listing details
    list_display_links = ('id', 'title')  # Links to listing (id, title) in the admin area to make it clickable
    list_filter = ('realtor',)  # Filter by realtor
    list_editable = ('is_published',)  # Publish/ Unpublish
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25  # Number of listings per page


admin.site.register(Listing, ListingAdmin)
