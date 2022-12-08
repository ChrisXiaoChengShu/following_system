from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_list/', views.user_list, name="user_list"),
    path("user/<str:pk>", views.user_page, name="user_page"),
    path("accounts/login/", auth_views.LoginView.as_view(), name='login'),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name='logout'),
]