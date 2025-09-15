
from django.urls import path
from student import views

urlpatterns = [
    path('cl1', views.MyClassView1.as_view(), name='myclassview'),
    path('cl2', views.MyClassView2.as_view(), name='myclassview2'),
    path('cl3', views.MyClassView3.as_view(name='Rahul'), name='myclassview3'),
    path('chcl3', views.MychildClassView3.as_view(), name='mychildClassview3'),
    path('homecl', views.HomeClassView.as_view() , name='homeclassview'),
    path('aboutcl', views.HomeClassView.as_view() , name='aboutclassview'),
]
