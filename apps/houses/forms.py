from django import forms

class RegForm(forms.Form):
    name = forms.CharField(label="What is thine name?", max_length=254)
    email = forms.EmailField(label="How may we summon you on the interweb?")
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_pw = forms.CharField(widget=forms.PasswordInput, label="Confirm Password Please")

