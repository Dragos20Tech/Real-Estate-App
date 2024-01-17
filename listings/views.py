from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from .models import Listing
from .choices import state_choices, price_choices, bedroom_choices


# Create your views here.

def index(request):

    paginator = Paginator(Listing.objects.order_by('-list_date').filter(is_published=True), 6)
    page = request.GET.get('page')  # URL parameter
    paged_listings = paginator.get_page(page)  # returns a page object

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)  # returns a model object or raises 404 error

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices
    }

    return render(request, 'listings/search.html', context)
