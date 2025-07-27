from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
      