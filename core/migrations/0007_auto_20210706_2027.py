# Generated by Django 2.1.7 on 2021-07-06 23:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210706_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 7, 6, 20, 27, 31, 428855)),
        ),
    ]
