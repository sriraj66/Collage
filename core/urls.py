from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path("",index,name='index'),
    path("auth/register/",register,name='register'),
    path("auth/login/",Login,name='login'),
    path("auth/logout/",Logout,name='logout'),
    path("auth/profile/",Profile,name='profile')
]