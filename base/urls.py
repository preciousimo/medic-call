from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontend, name="frontend"),
    path('backend/', views.backend, name="backend"),
]