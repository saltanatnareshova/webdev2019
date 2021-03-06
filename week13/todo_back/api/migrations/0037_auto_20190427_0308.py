# Generated by Django 2.2 on 2019-04-26 21:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0036_auto_20190427_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 4, 27, 3, 7, 58, 940302)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 4, 27, 3, 7, 58, 940302)),
        ),
    ]
