
from django.urls import path

from journey2app import views

urlpatterns = [

    path('',views.demo,name='demo'),
    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('logout',views.logout,name='logout'),
]
