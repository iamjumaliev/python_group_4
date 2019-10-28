from django.contrib.auth.models import User

from django import forms
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput)

    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)

    email = forms.EmailField(label='email', required=True)

    def clean_password_confirm(self):

        password = self.cleaned_data.get("password")

        password_confirm = self.cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')

        return password_confirm

    def save(self, commit=True):

        user = super().save(commit=False)

        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user

    def clean(self):
        super().clean()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if not first_name and not last_name:
            raise ValidationError('Error, first or last name must be filled', code='name_is_empty')
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('Email already registered.', code='email_registered')
        except User.DoesNotExist:
            return email

    class Meta:

        model = User

        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name' , 'email']