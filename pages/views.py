from django.shortcuts import render


# Django's views are Python functions that takes http requests and returns http response, like HTML documents.
# A web page that uses Django is full of views with different tasks and missions.

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')
