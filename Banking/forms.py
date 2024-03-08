from django import forms

class Login(forms.Form):
    username = forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={'class': 'form-control hide-label', 'placeholder': 'name@email.com'}))
    password = forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={'class': 'form-control hide-label','type':'password', 'placeholder': 'name@1234'}))

class Field(forms.Form):
    tag = forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={'class': 'form-control hide-label','type':'text', 'placeholder': 'tag','aria-describedby':"basic-addon1",'max-width': '95%','transform': 'translateX(2%)'}))
    cvv = forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={'class': 'form-control hide-label','type':'password', 'placeholder': '123','max-width': '95%','transform': 'translateX(2%)'}))
    amt = forms.IntegerField(label='',widget=forms.TextInput(attrs={'class': 'form-control hide-label','type':'text', 'placeholder': '999999999999','aria-describedby':"basic-addon1",'max-width': '95%','transform': 'translateX(2%)'}))