# Generated by Django 3.2.3 on 2021-08-29 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prerregistro', '0004_prerregistro_usuario_db'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prerregistro',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]