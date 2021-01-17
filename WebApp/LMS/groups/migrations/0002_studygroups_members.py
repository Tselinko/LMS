# Generated by Django 3.1.4 on 2021-01-17 20:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='studygroups',
            name='members',
            field=models.ManyToManyField(limit_choices_to={'is_staff': False}, related_name='member_group', to=settings.AUTH_USER_MODEL, verbose_name='Учашиеся группы'),
        ),
    ]
