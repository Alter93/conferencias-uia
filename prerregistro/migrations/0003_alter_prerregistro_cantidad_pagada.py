# Generated by Django 3.2.3 on 2021-08-27 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prerregistro', '0002_alter_prerregistro_comunidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prerregistro',
            name='cantidad_pagada',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
