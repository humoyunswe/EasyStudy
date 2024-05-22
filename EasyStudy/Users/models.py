from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    language = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    price_min = models.DecimalField(max_digits=6, decimal_places=2)
    price_max = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    specialties = models.TextField()
    resume = models.TextField()
    certificate = models.FileField(upload_to='certificates')
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
