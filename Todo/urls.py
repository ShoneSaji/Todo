"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from work_app.views import Registration,Logging,Add_Task,Delete_Task,Task_Edit,Signout,User_Delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',Registration.as_view(),name="home"),
    path('log/',Logging.as_view(),name="login"),
    path('',Add_Task.as_view(),name="add"),
    path('delete/<int:pk>',Delete_Task.as_view(),name="delete"),
    path('add/update/<int:pk>',Task_Edit.as_view(),name="edit"),
    path('signout/',Signout.as_view(),name="logout"),
    path('dele/<int:pk>',User_Delete.as_view(),name="del"),
]
