# Generated by Django 2.2.10 on 2020-07-28 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200728_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dataentrega',
            field=models.DateField(blank=True, null=True, verbose_name='Data da entrega'),
        ),
    ]
