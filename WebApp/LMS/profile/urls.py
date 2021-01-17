from django.urls import path
from . import views

urlpatterns = [
    path('login', views.MyProjectLoginView.as_view(), name='login'),
    path('registration', views.MyProjectRegistrView.as_view(), name='registration'),
    path('logout', views.MyProjectLogout.as_view(), name='logout'),
    path('<slug:login>/settings', views.ProfileSettingsView.as_view(), name='profile-settings'),
    path('<slug:login>', views.ProfileView.as_view(), name='profile'),
    path('password/', views.PasswordsChangeView.as_view(template_name='profile/change-password.html')),
]
