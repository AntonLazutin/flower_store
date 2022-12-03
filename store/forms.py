from django import forms
from . import models

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        return super(SignUpForm, self).save()


class FlowerForm(forms.ModelForm):

    class Meta:
        model = models.Flower
        exclude = ('id', )


class OrderForm(forms.ModelForm):

    class Meta:
        model = models.Order
        exclude = ['id', 'is_done', 'customer', 'flower',]