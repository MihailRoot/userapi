# Generated by Django 4.2.2 on 2023-06-26 16:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_newsletter_filternumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='filternumber',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]