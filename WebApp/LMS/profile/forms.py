from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile
import re


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Profile
        fields = ('login', 'email', 'name', 'surname', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('begin_year', 'degree', 'form', 'pay', 'avatar', 'phone_number', 'vk_url', 'fb_url', 'linkedin_url', 'instagram_url')

    def clean_phone_number(self):
        try:
            data = self.cleaned_data.get('phone_number')
            rule = re.compile(r'(^[+0-9]{1,3})*([0-9]{10,11}$)')
            if not rule.search(data):
                raise forms.ValidationError('Некорректно введен номер телефона')
            return data
        except TypeError:
            pass

    def clean_vk_url(self):
        try:
            data = self.cleaned_data.get('vk_url')
            rule = re.compile(r'https://vk.com/\S{1,50}')
            if not rule.search(data):
                raise forms.ValidationError('Некорректная ссылка на профиль VK')
            return data
        except TypeError:
            pass

    def clean_fb_url(self):
        try:
            data = self.cleaned_data.get('fb_url')
            rule = re.compile(r'https://www.facebook.com/\S{1,50}')
            if not rule.search(data):
                raise forms.ValidationError('Некорректная ссылка на профиль Facebook')
            return data
        except TypeError:
            pass

    def clean_linkedin_url(self):
        try:
            data = self.cleaned_data.get('linkedin_url')
            rule = re.compile(r'https://http://www.linkedin.com/\S{1,50}')
            if not rule.search(data):
                raise forms.ValidationError('Некорректная ссылка на профиль LinkedIn')
            return data
        except TypeError:
            pass

    def clean_instagram_url(self):
        try:
            data = self.cleaned_data.get('instagram_url')
            rule = re.compile(r'https://www.instagram.com/\S{1,50}')
            if not rule.search(data):
                raise forms.ValidationError('Некорректная ссылка на профиль Instagram')
            return data
        except TypeError:
            pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class PasswordChangingForm(PasswordChangeForm):
    class Meta:
        model = Profile
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'