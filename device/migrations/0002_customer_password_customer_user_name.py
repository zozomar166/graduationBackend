# Generated by Django 4.2.1 on 2023-05-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='user_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]