from django.urls import path, re_path

from App2 import views

urlpatterns = [
    re_path('kira/', views.response),
]
