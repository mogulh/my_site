from django.contrib.auth.models import User
from django.db import models

# Create your models here.
types = [
    ('web development', 'web development'),
    ('marketing', 'marketing'),
    ('consultation', 'consultation'),
]

duration_type = [
    ('month(s)', 'months(s)'),
    ('week(s)', 'week(s)'),
    ('year(s)', 'year(s)'),
]

start_typ = [
    ('month(s)', 'months(s)'),
    ('week(s)', 'week(s)'),
    ('year(s)', 'year(s)'),
]


class Inquiry(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=100)
    services = models.CharField(choices=types, max_length=20)
    message = models.CharField(max_length=256)
    time = models.DateTimeField(auto_now_add=True)


class Business(models.Model):
    status = [
        ('starting', 'starting'),
        ('achieving sales', 'achieving sales'),
        ('expansion', 'expansion'),
    ]
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business')
    email = models.EmailField()
    business_name = models.CharField(max_length=200, blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)
    stage = models.CharField(max_length=100, choices=status, default='starting')
    paid_ads = models.BooleanField(default=False)
    marketing_channels = models.CharField(max_length=200, blank=True, null=True)


class Domain(models.Model):
    status = [
        ('dormant', 'dormant'),
        ('active no sales', 'active no sales'),
        ('with sales', 'with sales'),
    ]

    business = models.OneToOneField(Business, on_delete=models.CASCADE)
    domain = models.URLField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, choices=status, default='dormant')


class Subscription(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField()
    sub_to = models.CharField(choices=types, default='all', max_length=20)


class Vision(models.Model):
    target_type = [
        ('web traffic', 'web traffic'),
        ('subscriptions', 'subscriptions'),
        ('sales', 'sales'),
    ]
    business = models.OneToOneField(Business, on_delete=models.CASCADE)
    duration = models.PositiveSmallIntegerField()
    duration_type = models.CharField(choices=duration_type, max_length=20)
    target = models.PositiveSmallIntegerField()
    target_type = models.CharField(choices=target_type, max_length=20)
    start = models.PositiveSmallIntegerField()
    start_type = models.CharField(choices=start_typ, max_length=20)
