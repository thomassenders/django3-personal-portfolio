# Generated by Django 3.0.8 on 2020-08-04 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='url',
        ),
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.date(2020, 8, 4)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
