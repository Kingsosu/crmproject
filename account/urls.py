from django.urls import path
from account import views as v
from django.contrib.auth import views as auth_views

app_name ='account'

urlpatterns = [
    path('register/', v.register, name='register'),
    path('my_login/', v.my_login, name='my_login'),   
    path('user_logout/', v.user_logout, name='user_logout')
]
