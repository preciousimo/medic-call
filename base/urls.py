from django.urls import path
from . import views

urlpatterns = [
    #Path to login and logout
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    
    #Path to access the frontend page
    path('', views.frontend, name="frontend"),
    #Path to access the backend page
    path('backend/', views.backend, name="backend"),

    #Path to add patient
    path('add_patient/', views.add_patient, name="add_patient"),
    #Path to access the patient individually
    path('patient/<str:patient_id>/', views.patient, name="patient"),
    #Path to edit patient details
     path('edit_patient/', views.edit_patient, name="edit_patient"),
     
    #Path to eelete the patient
    path('delete_patient/<str:patient_id>/', views.delete_patient, name="delete_patient"),
]