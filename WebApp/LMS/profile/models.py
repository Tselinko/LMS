from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


class Profile(AbstractBaseUser, PermissionsMixin):
    choices_1 = (
        ('Бакалавр', 'Бакалавр'),
        ('Специалист', 'Специалист'),
        ('Магистр', 'Магистр'),
    )
    choices_2 = (
        ('Очная', 'Очная'),
        ('Заочная', 'Заочная'),
        ('Вечерняя', 'Вечерняя'),
    )
    choices_3 = (
        ('Бюджетная', 'Бюджетная'),
        ('Контрактная', 'Контрактная'),
    )

    email = models.EmailField('email адрес', unique=True)
    login = models.CharField('Логин на сайте', unique=True, max_length=50)
    name = models.CharField('Имя', max_length=50, default='')
    begin_year = models.CharField('Год поступления', max_length=10, default='')
    surname = models.CharField('Фамилия', max_length=50, default='')
    degree = models.CharField('Степень', max_length=50, choices=choices_1, default='')
    form = models.CharField('Форма обучения', max_length=50, choices=choices_2, default='')
    pay = models.CharField('Основа обучения', max_length=50, choices=choices_3, default='')
    avatar = models.ImageField('Аватар', upload_to="images/profile/", default="images/profile/blank-avatar.jpg")
    phone_number = models.CharField('Номер телефона', max_length=50, null=True, blank=True)
    vk_url = models.CharField('Ссылка на профиль VK', max_length=50, null=True, blank=True)
    fb_url = models.CharField('Ссылка на профиль Facebook', max_length=50, null=True, blank=True)
    linkedin_url = models.CharField('Ссылка на профиль LinkedIn', max_length=50, null=True, blank=True)
    instagram_url = models.CharField('Ссылка на профиль Instagram', max_length=50, null=True, blank=True)
    is_teacher = models.BooleanField('Флаг учителя', default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['login']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return f'/profile/{self.login}'


