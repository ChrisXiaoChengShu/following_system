from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_list/', views.user_list, name="user_list"),
    path("user/<str:pk>", views.user_page, name="user_page"),
]