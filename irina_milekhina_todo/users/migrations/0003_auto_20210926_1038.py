# Generated by Django 3.1 on 2021-09-26 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210901_2157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('pk',), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
