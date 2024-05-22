from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
    Teachers = models.Profile.objects.all()
    return render(request, 'users/student_list.html', {'Teachers': Teachers})