from django.contrib import admin
from .models import  Newsletter, Contact_us_Message, IntrestedClient, Invoice
# Register your models here.
admin.site.register(Newsletter)
admin.site.register(Contact_us_Message)
admin.site.register(IntrestedClient)
admin.site.register(Invoice)
