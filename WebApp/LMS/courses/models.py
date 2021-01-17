from django.db import models
from profile.models import Profile
import datetime
from django.utils import timezone


class Courses(models.Model):
    title = models.CharField('Название курса', max_length=150, default='')
    anons = models.TextField('Анонс курса', max_length=1000, default='')
    description = models.TextField('Описание курса', max_length=10**6, default='')
    teachers = models.ManyToManyField(Profile, verbose_name='Преподаватели курса', related_name='teachers', limit_choices_to={'is_teacher':  True})
    confidants = models.ManyToManyField(Profile, verbose_name='Доверенные лица', related_name='confidants', limit_choices_to={'is_teacher':  False})
    course_avatar = models.ImageField('Аватар курса', upload_to="images/courses/", default="images/courses/py.png")

    def __str__(self):
        return f'Курс: {self.title}'

    def get_absolute_url(self):
        return f'/courses/{self.id}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Materials(models.Model):
    course = models.ForeignKey(Courses, verbose_name='Курс', related_name="materials", related_query_name="course", on_delete=models.CASCADE)
    title = models.CharField('Название материала', max_length=150, default='')
    description = models.TextField('Описание материала', max_length=250, default='')
    material_сontent = models.TextField('Материал', max_length=10 ** 6, default='')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return f'Материал курса: {self.title}'

    def get_absolute_url(self):
        return f'/courses/materials/{self.id}'

    class Meta:
        ordering = ['-date']
        verbose_name = 'Материалы курса'
        verbose_name_plural = 'Материалы курсов'


class Homeworks(models.Model):
    course = models.ForeignKey(Courses, verbose_name='Курс', related_name="homeworks", on_delete=models.CASCADE)
    deadline = models.DateTimeField('Срок сдачи', null=True, blank=True)
    date_of_beggining = models.DateTimeField('Дата начала выполнения', default=datetime.datetime.now())
    title = models.CharField('Название домашнего задания', max_length=150, default='')
    description = models.TextField('Описание домашнего задания', max_length=1000, default='')

    def __str__(self):
        return f'Домашнее задание: {self.title}'

    def get_absolute_url(self):
        return f'/courses/homeworks/{self.id}'

    def get_date(self):
        if self.deadline is not None:
            now = datetime.datetime.now()
            now = timezone.now()
            return (self.deadline >= now)
        else:
            return True

    def get_begin_date(self):
        if self.date_of_beggining is not None:
            now = datetime.datetime.now()
            now = timezone.now()
            return (self.date_of_beggining <= now)
        else:
            return True

    class Meta:
        ordering = ['-date_of_beggining']
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'


class StudentsHomeworks(models.Model):
    homework = models.ForeignKey(Homeworks, verbose_name='Задание', related_name="solution", on_delete=models.CASCADE)
    material = models.TextField('Материал домашней работы', default='')
    date = models.DateTimeField('Дата сдачи', auto_now_add=True)
    author = models.ForeignKey(Profile, verbose_name='Автор', related_name="author", on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = 'Домашнее задание студента'
        verbose_name_plural = 'Домашние задания студентов'

    def __str__(self):
        return f'{self.homework.title} от {self.author}'


