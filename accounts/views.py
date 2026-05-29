from django.shortcuts import render
from django.conf import settings
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required




# Login Page View
def login_page(request):
    return render(request, 'accounts/login.html', {'google_client_id': settings.GOOGLE_CLIENT_ID})

# Authentication Token Receiver View
@csrf_exempt
def auth_receiver(request):
    body = json.loads(request.body)
    token = body.get('credential')
    
    try:
        user_info = id_token.verify_oauth2_token(
            token,
            google_requests.Request(),
            settings.GOOGLE_CLIENT_ID
        )

        print ("User Info:", user_info)

        user, created = User.objects.get_or_create(
            username = user_info['email'],
            defaults = {
                'email' : user_info['email'],
                'first_name' : user_info['given_name'],
                'last_name' : user_info['family_name'],
            }
        )

        login(request, user)

        return JsonResponse({'status': 'ok', 'redirect': '/accounts/home/'})

    except ValueError:
        return JsonResponse({'status': 'error'}, status = 403)
    

@login_required
def home(request):
    return render(request, 'accounts/home.html')