# Generated by Django 4.2.1 on 2023-06-06 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('V1', '0006_alter_customer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='status',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], default='0', max_length=1),
        ),
    ]
