# Generated by Django 3.2.5 on 2021-07-04 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
