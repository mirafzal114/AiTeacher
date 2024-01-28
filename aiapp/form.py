from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from aiapp.models import FeedBack


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['feedback']
        widgets = {
            'feedback': forms.Textarea(attrs={'cols': 80, 'rows': 5}),}