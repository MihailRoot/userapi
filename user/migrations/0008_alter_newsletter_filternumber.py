# Generated by Django 4.2.2 on 2023-06-26 16:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_newsletter_filternumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='filternumber',
            field=models.ManyToManyField(db_column='kode', to=settings.AUTH_USER_MODEL),
        ),
    ]