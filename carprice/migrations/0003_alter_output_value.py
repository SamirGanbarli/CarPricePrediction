# Generated by Django 4.0.2 on 2022-02-25 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carprice', '0002_output'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output',
            name='value',
            field=models.CharField(max_length=50, verbose_name='value'),
        ),
    ]
