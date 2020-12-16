from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Subscription)
admin.site.register(Domain)
admin.site.register(Business)
admin.site.register(Inquiry)
admin.site.register(Vision)

