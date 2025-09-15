
from django.urls import path
from django.views.generic.base import TemplateView
from student import views

urlpatterns = [
    # path('home/', TemplateView.as_view(template_name='student/home.html'), name='home'),
    # path('index', views.TemplateView.as_view(template_name='student/index.html'), name='viewhome')
    path('index', views.AboutTemplateView.as_view(), name='viewhome'),
    # path('contact', views.ContactTemplateView.as_view(), name='contacttemplate'),
    path('contact', views.ContactTemplateView.as_view(
      extra_context={'course':'Python'}),
      name='contacttemplate'),
    path('profile/<int:id>', views.ProfileTemplateView.as_view(), name='profile'),

]


