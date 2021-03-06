from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models

class gameForm(forms.Form):
  def save(self, user):
    number_instance = models.gameModel()
    number_instance.author = user
    number_instance.save()
    return number_instance

#Registration form adapted from class examples
class RegistrationForm(UserCreationForm):

  class Meta:
    model = User
    fields = ("username",
              "password1",
              "password2")

  def save(self, commit=True):
    user = super(RegistrationForm, self).save(commit=False)
    if commit:
      user.save()
    return user
