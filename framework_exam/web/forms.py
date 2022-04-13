import os

from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import UsernameField

from framework_exam.web.models import Photo

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", 'placeholder': 'Password',
                   'style': 'text-align: center;max-width: 300px;'})
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", 'placeholder': 'Password Confirmation',
                   'style': 'text-align: center;max-width: 300px;'})

    )

    class Meta:
        model = UserModel
        fields = ('email',)
        widgets = {
            'email': forms.TextInput(
                attrs={'placeholder': 'Email', 'style': 'text-align: center;max-width: 300px;'}),
        }
        labels = {
            'email': '',
        }


class UserLoginForm(auth_forms.AuthenticationForm):
    username = UsernameField(
        label='',
        widget=forms.TextInput(
            attrs={"autofocus": True, 'placeholder': 'Email', 'style': 'text-align: center;max-width: 300px;'}))
    password = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'placeholder': 'Password',
                                          'style': 'text-align: center;max-width: 300px;'}),
    )


class ChangePasswordForm(auth_forms.PasswordChangeForm):
    old_password = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True, 'placeholder': 'Old Password',
                   'style': 'text-align: center;max-width: 300px;'}
        ),
    )
    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", 'placeholder': 'New Password',
                   'style': 'text-align: center;max-width: 300px;'})
    )
    new_password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", 'placeholder': 'New Password Confirmation',
                   'style': 'text-align: center;max-width: 300px;'})

    )


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo', 'description')
        widgets = {
            'description': forms.TextInput(
                attrs={'placeholder': 'Write down the description of your favourite photo.',
                       'maxlength': '475', 'style': 'text-align: center;'}),
        }
        labels = {
            'photo': '',
            'description': '',
        }


class DeletePhotoForm(forms.ModelForm):
    def save(self, commit=True):
        os.remove(self.instance.photo)
        self.instance.delete()
        return self.instance

    class Meta:
        model = Photo
        exclude = ('user',)
