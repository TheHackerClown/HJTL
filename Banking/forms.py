from django import forms

class Login(forms.Form):
    username = forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={'class': 'form-control hide-label', 'placeholder': 'name@email.com','id':'floatingInput'}))
    password = forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={'class': 'form-control hide-label','type':'password', 'placeholder': 'name@1234','id':'floatingPassword'}))

class Field(forms.Form):
    tag = forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={'class': 'form-control hide-label','type':'text', 'placeholder': 'tag','aria-describedby':"tag",'id':'tag'}))
    cvv = forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={'class': 'form-control hide-label','type':'password', 'placeholder': '123','id':'cvv'}))
    amt = forms.IntegerField(label='',widget=forms.TextInput(attrs={'class': 'form-control hide-label','type':'text', 'placeholder': '999999999999','aria-describedby':"amt",'id':'amt'}))