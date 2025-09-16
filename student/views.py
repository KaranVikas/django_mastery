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
  ordering=['roll']
  context_object_name = 'all_students'

  # add query parameter in Generic View - List View
  def get_queryset(self):
    return Student.objects.filter(course='Python')
  
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['django_students'] = Student.objects.filter(course='Django')
    print("context", context['django_students'])
    return context
  
  # conditional rendering templates 
  def get_templates_names(self):
    if self.request.COOKIES.get('user') == 'sonam':
      template_name = 'student/home.html'
    else: 
      template_name = 'student/profile.html'
    return [template_name]


