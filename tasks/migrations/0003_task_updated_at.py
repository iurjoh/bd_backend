# Generated by Django 3.2.20 on 2023-09-23 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20230917_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]