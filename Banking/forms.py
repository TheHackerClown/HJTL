from django import forms

class Login(forms.Form):
    username = forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={'class': 'form-control hide-label', 'placeholder': 'name@email.com'}))
    password = forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={'class': 'form-control hide-label','type':'password', 'placeholder': 'name@1234'}))