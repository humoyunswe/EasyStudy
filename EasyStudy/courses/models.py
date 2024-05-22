from django.db import models

# Create your models here.

from django.db import models
from users.models import TeacherProfile

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, related_name='courses')
    language = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_hours = models.PositiveIntegerField()

    def __str__(self):
        return self.title
