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

    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)

    # Keywords
    if 'keywords' in request.GET:  # if keywords is in request
        keywords = request.GET['keywords']  # GET returns a dictionary
        if keywords:  # if keywords is not empty string
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)  # iexact ignores case sensitivity

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']  # It is looking at the form field named 'bedrooms'
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)  # lte = less than or equal to

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    # The name attribute is the most important when submitting a form!
    # Of course the action of the form tag because that tells where to submit to.

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'listings': queryset_list
    }

    return render(request, 'listings/search.html', context)
