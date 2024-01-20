from django.urls import path

from . import views

# URLconf object
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]

# Each 'path' function within the list represents a URL pattern that the Django application can handle.
# The arguments to the path function include the URL pattern as a string and the corresponding view function
# that should be called when that URL is accessed.
