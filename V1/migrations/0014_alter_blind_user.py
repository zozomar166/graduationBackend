# Generated by Django 4.2.1 on 2023-06-22 23:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('V1', '0013_alter_device_blind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blind',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blinds', to=settings.AUTH_USER_MODEL),
        ),
    ]
