from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator


class Student(models.Model):
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=100)
    email = models.EmailField("Email", validators=[EmailValidator()])
    language = models.CharField("Language", max_length=100)
    age = models.IntegerField("Age", validators=[MinValueValidator(5), MaxValueValidator(120)])
    price_min = models.DecimalField("Minimum Price", max_digits=7, decimal_places=2, validators=[MinValueValidator(0)])
    price_max = models.DecimalField("Maximum Price", max_digits=7, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['last_name', 'first_name']


class Teacher(models.Model):
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=100)
    email = models.EmailField("Email", validators=[EmailValidator()])
    specialties = models.TextField("Specialties")
    resume = models.TextField("Resume")
    certificate = models.FileField("Certificate", upload_to='certificates',blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
        ordering = ['last_name', 'first_name']
