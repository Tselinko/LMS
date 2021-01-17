from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Profile


class ProfileAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Profile
    list_display = ('email', 'is_teacher', 'is_staff', 'is_active', 'login', 'name', 'surname', 'begin_year', 'degree', 'form', 'pay', 'avatar',)
    list_filter = ('email', 'is_staff', 'is_active', 'is_teacher')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'surname', 'begin_year', 'degree', 'form', 'pay', 'avatar', 'login', )}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_teacher',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'login', 'name', 'surname', 'is_teacher', 'begin_year', 'degree', 'form', 'pay', 'avatar',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Profile, ProfileAdmin)
