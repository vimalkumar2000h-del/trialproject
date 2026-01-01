from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student'),
    path('teachers/', views.teacher_list, name='teacher'),
]
