# Generated by Django 3.1.4 on 2021-01-17 20:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210117_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeworks',
            name='date_of_beggining',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 17, 23, 6, 34, 906304), verbose_name='Дата начала выполнения'),
        ),
    ]
