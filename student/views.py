from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from student.models import Student
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

# Create your views here.
# Simple class based View
# class AllStudentView(View):
#   def get(self, request):
#     all_students = Student.objects.all()
#     return render(request, 'student/all_student.html',{
#       'all_students':all_students
#     })

class StudentListView(ListView):
  model = Student
  

