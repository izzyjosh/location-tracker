from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationForm(UserCreationForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


    username = forms.CharField(
           label="",
           help_text="",
           widget = forms.TextInput(attrs={
               "name":"username",
               "type":"text",
               "placeholder":"Username",
               "id":"username",
               }
            )
        )

    email = forms.EmailField(
           label="",
           widget = forms.TextInput(attrs={
               "name":"email",
               "type":"email",
               "placeholder":"Email",
               "id":"email",
               }
        )
    )

    password1 = forms.CharField(
           label="",
           help_text="",
           widget=forms.PasswordInput(attrs={
               "name":"password1",
               "id":"password",
               "placeholder":"Password",
               "type":"password",
               }
        )
    )

    password2 = forms.CharField(
           label="",
           help_text="",
           widget=forms.PasswordInput(attrs={
               "name":"password2",
               "id":"password",
               "placeholder":"Confirm Password",
               "type":"password",
               }
            )
        )


    class Meta:
        model = User
        fields = ("username","email")

