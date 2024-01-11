from django.urls import path

from . import views

# URLconf object
urlpatterns = [
    path('', views.index, name='listings'),  # path function returns a URLPattern object
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]
