from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, StudentProfile, TeacherProfile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

class StudentProfileInline(admin.StackedInline):
    model = StudentProfile
    can_delete = False

class TeacherProfileInline(admin.StackedInline):
    model = TeacherProfile
    can_delete = False

class CustomUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, StudentProfileInline, TeacherProfileInline)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        if obj.profile.user_type == 'student':
            return [ProfileInline(self.model, self.admin_site), StudentProfileInline(self.model, self.admin_site)]
        elif obj.profile.user_type == 'teacher':
            return [ProfileInline(self.model, self.admin_site), TeacherProfileInline(self.model, self.admin_site)]
        else:
            return [ProfileInline(self.model, self.admin_site)]

# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'location')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'language', 'age', 'price_min', 'price_max')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialties', 'hourly_rate')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
