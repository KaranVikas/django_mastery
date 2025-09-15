from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from student.models import Profile

# Create your views here.
class MyClassView1(View):
  def get(self, request):
    return HttpResponse("Hello Class based view")
  
class MyClassView2(View):
  def get(self, request):
    return HttpResponse("<h1>Class based view </h1>")

class MyClassView3(View):
  name = 'Sonam'
  def get(self, request):
    return HttpResponse(self.name)
  
class MychildClassView3(MyClassView3):
  def get(self, request):
    return HttpResponse(self.name)
  
class HomeClassView(View):
  def get(self, request):
    return render(request , 'student/all.html')
  
class AboutClassView(View):
  def get(self, request):
    context = {'msg': 'Welcome to mastering Django '}
    return render(request , 'student/all_html', context)
  

  
  

