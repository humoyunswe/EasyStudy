from django.contrib import admin

from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'language', 'price', 'duration_hours')
    search_fields = ('title', 'teacher__first_name', 'teacher__last_name')
    list_filter = ('language',)
