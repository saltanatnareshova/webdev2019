# Generated by Django 2.2 on 2019-04-26 19:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_auto_20190426_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 4, 27, 1, 34, 45, 462931)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 4, 27, 1, 34, 45, 462931)),
        ),
    ]
