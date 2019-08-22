from django.urls import path

from . import views

urlpatterns = [
    path('support/', views.users_check, name='users_check'),
    path('', views.index, name='index'),
]