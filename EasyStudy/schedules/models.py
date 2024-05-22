from django.db import models
from courses.models import Course
from users.models import TeacherProfile

class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='schedules')
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, related_name='schedules')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.course.title} by {self.teacher.first_name} at {self.start_time}'
