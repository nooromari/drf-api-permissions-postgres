# Generated by Django 3.2.4 on 2021-06-21 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='chef',
            new_name='author',
        ),
    ]
