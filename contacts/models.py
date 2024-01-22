from django.db import models


# Create your models here.
class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)  # blank=True means that the field is optional
    contact_date = models.DateTimeField(auto_now_add=True, blank=True)  # auto_now_add=True means that the field is
    # automatically populated with the current date and time
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
