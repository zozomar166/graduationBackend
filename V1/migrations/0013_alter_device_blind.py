# Generated by Django 4.2.1 on 2023-06-22 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('V1', '0012_alter_device_c_lat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='blind',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='device', to='V1.blind'),
        ),
    ]
