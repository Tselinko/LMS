# Generated by Django 3.1.4 on 2021-01-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_number', models.CharField(max_length=50, unique=True, verbose_name='Учебная группа')),
                ('study_year_number', models.IntegerField(default=1, verbose_name='Курс обучения')),
                ('department_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Факультет')),
                ('group_avatar', models.ImageField(default='images/groups/group_logo.jpg', upload_to='images/groups/', verbose_name='Эмблема группы')),
                ('courses', models.ManyToManyField(related_name='course_group', to='courses.Courses', verbose_name='Учебные курсы')),
            ],
            options={
                'verbose_name': 'Учебная группа',
                'verbose_name_plural': 'Учебные группы',
            },
        ),
    ]
