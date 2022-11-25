from django.contrib import admin
from .models import *
@admin.register(StatusJob)
class StatusJobAdmin(admin.ModelAdmin):
    list_display = ('id','status')
admin.site.register(Job)