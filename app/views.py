from django.shortcuts import render
from .models import Students

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def student_list(request):
    students = Students.objects.all()
    return render(request, 'app/student_list.html', {'students': students})

