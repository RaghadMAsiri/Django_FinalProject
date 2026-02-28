"""
URL configuration for core_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from courses import views as cour

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cour.course_list, name='course_list'),
    path('contact/', cour.contact_view, name='contact'), 
    path('add/<int:course_id>/', cour.add_to_list, name='add_to_list'),
    path('my-list/', cour.my_list, name='my_list'), 
    path('register/', cour.auth_register, name='register'),
    path('login/', cour.auth_login, name='login'),
    path('logout/', cour.auth_logout, name='logout'),
    path('checkout/', cour.checkout, name='checkout'),
]
