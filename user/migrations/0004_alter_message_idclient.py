# Generated by Django 4.2.2 on 2023-06-26 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_message_id_alter_newsletter_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='idclient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
