from django.urls import path

from . import views

# ------------- Path function arguments ----------------
# path(route, view, kwargs=None, name=None)
# -----------------------------------------------------

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),  # added the path for the about page
]
