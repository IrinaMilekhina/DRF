# Generated by Django 3.1 on 2021-09-01 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todo_created_by_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created_by_user',
        ),
    ]