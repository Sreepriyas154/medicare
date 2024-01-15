from django  import forms
from django.contrib.auth.models import User
from api.models import user


class Loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"formcontrol"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"formcontroler"}))


class Registrationform(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"formcontroll"}),
            "last_name":forms.TextInput(attrs={"class":"formcontroll"}),
            "email":forms.EmailInput(attrs={"class":"formcontroll"}),
            "username":forms.TextInput(attrs={"class":"formcontroll"}),
            "password":forms.PasswordInput(attrs={"class":"formcontroll"})
        }