import json

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    return render(request, 'clients/home.html')


def start(request):
    return render(request, 'clients/start.html')


def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        try:
            user = User.objects.create_user(username=email, password=email, email=email)


        except:
            user = User.objects.get(username=email)
            print(user.username)
            user.save()

        response = {'status': 1, 'message': "Ok"}  # for ok
        login(request, user)

        return HttpResponse(json.dumps(response), content_type='application/json')



