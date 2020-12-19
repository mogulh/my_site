import json

from django.contrib.auth import login
from django.contrib.auth.models import User, Group
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import *


def home(request):
    return render(request, 'clients/home.html')


def start(request):
    return render(request, 'clients/start.html')


def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        user_type = data['type']
        print(data)

        try:
            user = User.objects.create_user(username=email, password=email, email=email)
            user.save()
            print(user.username)


        except:
            user = User.objects.get(username=email)
            print(user.username)
            user.save()

        response = {'status': 1, 'message': "Ok"}  # for ok
        login(request, user)
        group = Group.objects.get(name=user_type)
        user.groups.add(group)

        return HttpResponse(json.dumps(response), content_type='application/json')


def bizna(request):
    if request.method == 'POST':
        client = request.user
        email = client.email
        data = json.loads(request.body)

        business_name = data['biz']
        industry = data['industry']
        stage = data['stage']
        paid_ads = data['ads']
        marketing_channels = data['channels']

        biz = Business.objects.create(client=client,
                                      email=email,
                                      business_name=business_name,
                                      industry=industry,
                                      stage=stage,
                                      paid_ads=paid_ads,
                                      marketing_channels=marketing_channels)
        biz.save()
        response = {'status': 1, 'message': "Ok"}  # for ok

        return HttpResponse(json.dumps(response), content_type='application/json')


def domain(request):
    if request.method == 'POST':
        client = request.user
        business = client.business.latest('pk')
        data = json.loads(request.body)

        domain = data['domain']
        status = data['status']

        biz = Domain.objects.create(
            business=business,
            domain=domain,
            status=status)
        biz.save()
        response = {'status': 1, 'message': "Ok"}  # for ok

        return HttpResponse(json.dumps(response), content_type='application/json')


def vision(request):
    if request.method == 'POST':
        client = request.user
        business = client.business.latest('pk')
        data = json.loads(request.body)

        duration = data['duration']
        duration_type = data['duration_type']
        target = data['target']
        target_type = data['target_type']
        start = data['start']
        start_type = data['start_type']

        viz = Vision.objects.create(
            duration=duration,
            duration_type=duration_type,
            target=target,
            target_type=target_type,
            start=start,
            start_type=start_type,
            business=business,

        )
        viz.save()
        response = {'status': 1, 'message': "Ok"}  # for ok

        return HttpResponse(json.dumps(response), content_type='application/json')


def inquiry(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        email = data['email']
        full_name = data['name']
        services = data['service']
        message = data['message']

        inq = Inquiry.objects.create(
            email=email,
            full_name=full_name,
            services=services,
            message=message,
        )
        inq.save()
        response = {'status': 1, 'message': "Ok"}  # for ok

        return HttpResponse(json.dumps(response), content_type='application/json')
