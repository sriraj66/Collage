from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path("",index,name='index'),
    path("auth/register/",register,name='register'),
    path("auth/login/",Login,name='login'),
    path("auth/logout/",Logout,name='logout'),
    path("auth/profile/",Profile,name='profile'),
    path("auth/passwordLink",Password_Link,name='pass_link'),
    path("auth/passwordReset/<str:token>",Password_reset,name='reset_pass'),
]