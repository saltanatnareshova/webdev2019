# Generated by Django 2.2 on 2019-04-27 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_auto_20190427_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 4, 27, 18, 26, 22, 696915)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 4, 27, 18, 26, 22, 696915)),
        ),
    ]
