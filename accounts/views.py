from django.shortcuts import render

# Create your views here.

# Login Page View
def login_page(request):
    return render(request, 'accounts/login.html')