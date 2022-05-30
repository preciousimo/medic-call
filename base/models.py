from email import message
from pyexpat import model
from django.db import models

# PATIENT
class Patient(models.Model):

    GENDER = (
        ('M', 'M'),
        ('F', 'F')
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# SUPPORT
OPTION = (
    ('It happened to me', 'It happened to me'),
    ('It was already like that', 'It was already like that'),
    )

REASON = (
    ('Delete patient','Delete patient'),
    ('System problems','System problems'),
    ('Others','Others'),
    )

SITUATION = (
    ('Done', 'Done'),
    ('Pending', 'Pending') ,    
    )

class Support(models.Model):
    
    terms = models.BooleanField("You got this responsibility")
    user = models.CharField(max_length=100)
    message = models.TextField()
    option = models.CharField(max_length=100, choices=OPTION)
    reason = models.CharField(max_length=100, choices=REASON)
    created_at = models.DateTimeField(auto_now_add=True)
    situation = models.CharField(max_length=100, null=True, choices=SITUATION, default='Pending')

    def __str__(self):
        return self.user
