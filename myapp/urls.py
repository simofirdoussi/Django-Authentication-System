from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registrationView, name="register"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutpage, name='logout'),
    path('', views.index, name='home'),
]