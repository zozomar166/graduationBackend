# Generated by Django 4.2.1 on 2023-05-18 15:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('api_key', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('ultrasonic_left_value', models.FloatField()),
                ('ultrasonic_right_value', models.FloatField()),
                ('gps_lat', models.FloatField()),
                ('gps_lng', models.FloatField()),
                ('gps_h', models.FloatField()),
                ('gps_m', models.FloatField()),
                ('gps_s', models.FloatField()),
                ('membership', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], default='0', max_length=1)),
            ],
        ),
    ]