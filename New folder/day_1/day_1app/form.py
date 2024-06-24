from django import forms
from day_1app.models import signup,login


class signup(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'


class login(forms.ModelForm):
    class Meta:
        model=login
        fields='__all__'
