"""Django_Demo_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from Django_Demo_App_1 import views as v1
from forms_app import views as v2

urlpatterns = [
    path('',v1.index,name="index"),
    # path('forms/',views.form_name,name='form')
    # path('other/',v1.other,name='other'),
    # path('relative/',v1.relative,name='relative'),
    path('', include('forms_app.urls')),
    path('Django_Demo_App_1/', include('Django_Demo_App_1.urls')),
    path('logout/',v1.user_logout,name='logout'),
    path('special/',v1.special,name='special'),
    path('admin/', admin.site.urls),
]
