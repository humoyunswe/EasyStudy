from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator

class UserType(models.Model):
  """
  Model to represent different user types (student, teacher)
  """
  TYPE_CHOICES = (
      ('student', 'Student'),
      ('teacher', 'Teacher'),
  )
  name = models.CharField(max_length=20, choices=TYPE_CHOICES)

  def __str__(self):
      return self.name

class StudentProfile(models.Model):
  """
  Model for student user profiles
  """
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
  language = models.CharField(max_length=100)
  age = models.PositiveIntegerField(validators=[MinValueValidator(13)])
  price_min = models.DecimalField(max_digits=6, decimal_places=2)
  price_max = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])

  def __str__(self):
      return f'{self.user.first_name} {self.user.last_name}'

class TeacherProfile(models.Model):
  """
  Model for teacher user profiles
  """
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
  specialties = models.TextField()
  resume = models.FileField(upload_to='resumes', allowed_extensions=['pdf', 'docx'])
  certificate = models.FileField(upload_to='certificates', allowed_extensions=['pdf', 'jpg', 'png'])
  hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)

  def __str__(self):
      return f'{self.user.first_name} {self.user.last_name}'
