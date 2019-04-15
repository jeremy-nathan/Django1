from django.urls import path
from forms_app import views

urlpatterns=[
        path('forms/',views.form_name,name='forms'),
]
