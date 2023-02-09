from django import forms
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ObjectDoesNotExist


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(label='confirm password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))

    class Meta:
        model = User
        exclude = ('password',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('passwords must be match')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            if user:
                raise ValidationError('this email is already exist')
        except ObjectDoesNotExist:
            return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        try:
            user = User.objects.get(phone_number=phone_number)
            if user:
                raise ValidationError('this phone number is already exist')
        except ObjectDoesNotExist:
            return phone_number

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="you can change password with <a href=\" ../password \">this form</a>")

    class Meta:
        model = User
        fields = '__all__'
