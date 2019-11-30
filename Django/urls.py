"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from Application import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.all, name='all' ),
    path('any/', views.save, name='save'),
    path('data/', views.data, name='data'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('Note/', views.NoteList.as_view()),
    path('Notes/<int:id>/', views.NoteDetial.as_view()),
]
