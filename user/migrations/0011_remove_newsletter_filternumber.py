# Generated by Django 4.2.2 on 2023-06-26 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_message_idclients_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='filternumber',
        ),
    ]
