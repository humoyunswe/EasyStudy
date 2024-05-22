from django.contrib import admin
from .models import UserType, StudentProfile, TeacherProfile

admin.site.register(UserType)

class StudentProfileAdmin(admin.ModelAdmin):
  list_display = ('user', 'user_type', 'language', 'age', 'price_min', 'price_max')
  search_fields = ('user__username', 'language', 'age')

admin.site.register(StudentProfile, StudentProfileAdmin)

class TeacherProfileAdmin(admin.ModelAdmin):
  list_display = ('user', 'user_type', 'specialties', 'hourly_rate')
  search_fields = ('user__username', 'specialties')

admin.site.register(TeacherProfile, TeacherProfileAdmin)
