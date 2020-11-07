from django.urls import path
from . import views

urlpatterns = [

    path('login', views.login, name='login-page'),
    path('register', views.register, name='registeration-page'),
    path('', views.home, name='loggedin-page'),
    path('logout', views.logout, name='logout-page'),
    path('profile', views.profile, name='profile')

]
