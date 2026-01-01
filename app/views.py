from django.shortcuts import render
from .models import Students

def student_list(request):
    students = Students.objects.all()
    return render(request, 'app/student_list.html', {'students': students})

