# Generated by Django 4.2.1 on 2023-06-01 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('V1', '0005_blind_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['id']},
        ),
    ]
