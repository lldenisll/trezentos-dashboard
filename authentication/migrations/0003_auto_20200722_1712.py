# Generated by Django 2.2.10 on 2020-07-22 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20200722_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='infoGeral',
            field=models.TextField(max_length=500),
        ),
    ]
