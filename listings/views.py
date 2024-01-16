from django.shortcuts import render
from .models import Listing


# Create your views here.

def index(request):
    context = {
        'listings': Listing.objects.all()  # this will return all the listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
