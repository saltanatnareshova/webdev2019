# Generated by Django 2.2 on 2019-04-21 12:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20190421_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 4, 21, 18, 38, 3, 870197)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 4, 21, 18, 38, 3, 870197)),
        ),
    ]