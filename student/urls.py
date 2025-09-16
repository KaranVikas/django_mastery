
from django.urls import path
from student import views

urlpatterns = [
    # path('', views.AllStudentView.as_view(), name='all_student')
    path('students/', views.StudentListView.as_view(), name='students')

]


