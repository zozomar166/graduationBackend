# Generated by Django 4.1.7 on 2023-05-28 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('V1', '0004_device_blind'),
    ]

    operations = [
        migrations.AddField(
            model_name='blind',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='blinds', to='user.user'),
            preserve_default=False,
        ),
    ]
