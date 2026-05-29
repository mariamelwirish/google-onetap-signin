from django.shortcuts import render
from django.conf import settings

# Create your views here.

# Login Page View
def login_page(request):
    return render(request, 'accounts/login.html', {'google_client_id': settings.GOOGLE_CLIENT_ID})