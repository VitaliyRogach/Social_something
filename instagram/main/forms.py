from django import forms
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': "Email"}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': "Username"}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': "Password"}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': "Repeat password"}))
    error_messages = UserCreationForm.error_messages
    error_messages['password_mismatch'] = 'Password incorrect.'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    error_messages = AuthenticationForm.error_messages
    error_messages['invalid_login'] = 'Enter a true login and password'

    class Meta:
        model = User
        fields = ['username', 'password']

# class RegisterUserForm(forms.ModelForm):
#     """
#     A form that creates a user, with no privileges, from the given username and
#     password.
#     """
#     error_messages = {
#         'password_mismatch': _('The two password fields didn’t match.'),
#     }
#     password1 = forms.CharField(
#         label=_("Password"),
#         strip=False,
#         widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
#         help_text=password_validation.password_validators_help_text_html(),
#     )
#     password2 = forms.CharField(
#         label=_("Password confirmation"),
#         widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
#         strip=False,
#         help_text=_("Enter the same password as before, for verification."),
#     )
#
#     class Meta:
#         model = User
#         fields = ("username",)
#         field_classes = {'username': UsernameField}
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self._meta.model.USERNAME_FIELD in self.fields:
#             self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError(
#                 self.error_messages['password_mismatch'],
#                 code='password_mismatch',
#             )
#         return password2
#
#     def _post_clean(self):
#         super()._post_clean()
#         # Validate the password after self.instance is updated with form data
#         # by super().
#         password = self.cleaned_data.get('password2')
#         if password:
#             try:
#                 password_validation.validate_password(password, self.instance)
#             except forms.ValidationError as error:
#                 self.add_error('password2', error)
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user