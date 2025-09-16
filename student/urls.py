
from django.urls import path
from django.views.generic.base import TemplateView, RedirectView
from student import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='student/home.html'), name='home'),
    path('home/', RedirectView.as_view(pattern_name='home'), name='home1'),
]


