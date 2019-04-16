from django.urls import path
from Django_Demo_App_1 import views

app_name='Django_Demo_App_1'

urlpatterns=[
        path('CBV/',views.IndexView.as_view()),
        path('life/',views.index,name='index'),
        path('other/',views.other,name='other'),
        path('relative/',views.relative,name='relative'),
        path('register/',views.register,name='register'),
        path('login/',views.user_login,name='login'),
]
