from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=7, choices=USER_TYPE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


class StudentProfile(Profile):
    language = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    price_min = models.DecimalField(max_digits=6, decimal_places=2)
    price_max = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class TeacherProfile(Profile):
    specialties = models.TextField()
    resume = models.TextField()
    certificate = models.FileField(upload_to='certificates')
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
