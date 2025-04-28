"""
URL configuration for taskmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  
]


# admin username: aavez
# admin password: 12django90
# admin email:aavez@gmail.com


{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1ODI0MTUyLCJpYXQiOjE3NDU4MjMyNTIsImp0aSI6IjQ1N2UxNTFkMWZiNTQyZDY4NjczNDI2NGRkMDk2N2E4IiwidXNlcl9pZCI6Mn0.JeH9V3cmVuczzG5BKMNTDanvfo74t6SkO-eOXbfUOFw",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTkwOTY1MiwiaWF0IjoxNzQ1ODIzMjUyLCJqdGkiOiJmMDljYTYyYmRhMDY0ODkzOWU5MWFmNDMyZjA3ZmQ2MiIsInVzZXJfaWQiOjJ9.jjGbbbwGUlgQuSYwhZDD41yeFXDXWi_heKM_Zdxg5VQ"
}