from django import forms

class UsernameForm(forms.Form):
    username = forms.CharField(label='Codeforces Username', max_length=100)
