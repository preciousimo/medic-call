from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    
    path('', views.frontend, name="frontend"),
    path('backend/', views.backend, name="backend"),
    path('add_patient/', views.add_patient, name="add_patient"),
    path('patient/<str:patient_id>/', views.patient, name="patient"),
]