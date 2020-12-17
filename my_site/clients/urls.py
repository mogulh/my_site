from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('start/', views.start, name='start'),
    path('biz/', views.bizna, name='biz'),
    path('dom/', views.domain, name='dom'),
    path('vision/', views.vision, name='vision'),
    path('inquiry/', views.inquiry, name='inquiry'),
]
