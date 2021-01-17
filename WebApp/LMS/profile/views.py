from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import CustomUserCreationForm, AuthUserForm, CustomUserChangeForm, PasswordChangingForm
from .models import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordChangeView


class MyProjectLoginView(LoginView):
    success_url = '/courses'
    template_name = 'profile/login.html'
    form_class = AuthUserForm

    def get_success_url(self):
        return self.success_url


class MyProjectRegistrView(CreateView):
    template_name = 'profile/registration.html'
    form_class = CustomUserCreationForm
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password1"]
        aut_user = authenticate(email=email, password=password)
        login(self.request, aut_user)
        return form_valid

    def get_absolute_url(self):
        return f'/profile/{self.login}'


class MyProjectLogout(LogoutView):
    next_page = '/profile/login'


class ProfileView(DetailView):
    model = Profile
    context_object_name = "profile"
    template_name = 'profile/profile.html'
    slug_field = 'login'
    slug_url_kwarg = 'login'


class ProfileSettingsView(UpdateView):
    model = Profile
    context_object_name = "profileset"
    template_name = 'profile/profile-settings.html'
    form_class = CustomUserChangeForm

    slug_field = 'login'
    slug_url_kwarg = 'login'


    #
    # def get_absolute_url(self):
    #     return f'/profile/{self.login}'


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = '/courses'





