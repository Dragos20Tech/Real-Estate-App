from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method == 'POST':
        # Register User

        return
        # # Testing
        # print('Submitted FORM', request.POST)
        # return redirect('register')
    else:
        return render(request, 'accounts/register.html')  # Login will submit to this


def login(request):
    if request.method == 'POST':
        # Login User
        return
    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    return redirect('listings:index')
