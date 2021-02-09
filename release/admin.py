from django.contrib import admin
from .models import Items, user, shipping_info
# Register your models here.
admin.site.register(Items)
admin.site.register(user)
admin.site.register(shipping_info)
