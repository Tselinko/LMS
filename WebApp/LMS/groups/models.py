from django.db import models
from courses.models import Courses
from profile.models import Profile


class StudyGroups(models.Model):
    group_number = models.CharField('Учебная группа', unique=True, max_length=50)
    study_year_number = models.IntegerField('Курс обучения', default=1)
    department_name = models.CharField('Факультет', max_length=150, blank=True, null=True)
    courses = models.ManyToManyField(Courses, verbose_name='Учебные курсы', related_name='course_group')
    members = models.ManyToManyField(Profile, verbose_name='Учашиеся группы', related_name='member_group', limit_choices_to={'is_teacher':  False})
    group_avatar = models.ImageField('Эмблема группы', upload_to="images/groups/", default="images/groups/group_logo.jpg")

    def __str__(self):
        return f'Группа: {self.group_number}'

    def get_absolute_url(self):
        return f'/groups/{self.id}/info'

    class Meta:
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'