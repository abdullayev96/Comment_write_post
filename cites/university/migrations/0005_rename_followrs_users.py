# Generated by Django 3.2.4 on 2023-06-01 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0004_auto_20230601_0837'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Followrs',
            new_name='Users',
        ),
    ]