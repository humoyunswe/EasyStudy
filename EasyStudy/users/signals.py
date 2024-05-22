from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Г, TeacherProfile

@receiver(post_save, sender=StudentProfile)
def create_student_profile(sender, instance, created, **kwargs):
  if created:
    # Create a corresponding user profile for the new student
    user_profile = UserProfile.objects.create(user=instance.user)
    # You can add additional actions here, like sending a welcome email or setting up default settings for the student

@receiver(post_save, sender=TeacherProfile)
def create_teacher_profile(sender, instance, created, **kwargs):
  if created:
    # Create a corresponding user profile for the new teacher
    user_profile = UserProfile.objects.create(user=instance.user)
    # You can add additional actions here, like sending a welcome email or setting up default settings for the teacher
