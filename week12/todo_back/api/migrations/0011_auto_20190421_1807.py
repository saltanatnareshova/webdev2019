# Generated by Django 2.2 on 2019-04-21 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20190421_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 4, 21, 18, 7, 14, 185861)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 4, 21, 18, 7, 14, 185861)),
        ),
    ]
