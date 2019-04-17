from django.urls import path
from Django_Demo_App_1 import views

app_name='Django_Demo_App_1'

urlpatterns=[
        path('list/',views.SchoolListView.as_view(),name='list'),
        path('list/<int:pk>/',views.SchoolDetailView.as_view(),name='details'),
        path('CBV/',views.IndexView.as_view()),
        path('life/',views.index,name='index'),
        path('other/',views.other,name='other'),
        path('relative/',views.relative,name='relative'),
        path('register/',views.register,name='register'),
        path('login/',views.user_login,name='login'),
        path('create/',views.SchoolCreateView.as_view(),name='create'),
        path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update'),
        path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='delete'),
        
]
