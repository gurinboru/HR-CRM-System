from django.contrib import admin
from .models import *
@admin.register(StatusJob)
class StatusJobAdmin(admin.ModelAdmin):
    list_display = ('id','status')

@admin.register(CallStatus)
class CallStatusAdmin(admin.ModelAdmin):
    list_display = ('id','status')

@admin.register(DenialStatus)
class DenialStatusAdmin(admin.ModelAdmin):
    list_display = ('id','status')

@admin.register(MeetStatus)
class MeetStatusAdmin(admin.ModelAdmin):
    list_display = ('id','status')

@admin.register(MeetEmpStatus)
class MeetEmpStatusAdmin(admin.ModelAdmin):
    list_display = ('id','status')

@admin.register(TestStatus)
class TestStatusAdmin(admin.ModelAdmin):
    list_display = ('id','status')

admin.site.register(Job)
admin.site.register(JobSeek)