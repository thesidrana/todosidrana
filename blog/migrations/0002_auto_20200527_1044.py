# Generated by Django 3.0.2 on 2020-05-27 05:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_posted',
        ),
        migrations.AddField(
            model_name='post',
            name='date_on',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
