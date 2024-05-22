from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Schedule

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('course', 'teacher', 'start_time', 'end_time', 'location')
    search_fields = ('course__title', 'teacher__first_name', 'teacher__last_name')
    list_filter = ('start_time', 'end_time')

