# Generated by Django 3.0.5 on 2020-05-27 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_group_head_of_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='head_of_group',
        ),
    ]
