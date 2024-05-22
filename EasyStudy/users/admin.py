from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, StudentProfile, TeacherProfile



class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class StudentProfileInline(admin.StackedInline):
    model = StudentProfile
    can_delete = False

class TeacherProfileInline(admin.StackedInline):
    model = TeacherProfile
    can_delete = False

class CustomUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        inlines = []
        if obj:
            try:
                profile = obj.profile
                inlines.append(ProfileInline(self.model, self.admin_site))
                if profile.user_type == 'student':
                    inlines.append(StudentProfileInline(self.model, self.admin_site))
                elif profile.user_type == 'teacher':
                    inlines.append(TeacherProfileInline(self.model, self.admin_site))
            except Profile.DoesNotExist:
                pass
        return inlines

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
