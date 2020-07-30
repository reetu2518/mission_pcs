from django.contrib import admin

# Register your models here.
from .models import staff,routine,time

admin.site.register(staff)
admin.site.register(routine)
admin.site.register(time)