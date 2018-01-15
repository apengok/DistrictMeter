
from django import forms

class JoinForm(forms.Form):
    email   = forms.EmailField()
    name    = forms.CharField(max_length=120)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email == 'apengok@163.com1':
            raise forms.ValidationError("this is super man")
        return email