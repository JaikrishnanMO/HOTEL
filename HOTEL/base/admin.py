from django.contrib import admin

from .models import Add_item,Admin_model,Today_item

# Register your models here.

admin.site.register(Add_item)
admin.site.register(Admin_model)
admin.site.register(Today_item)
