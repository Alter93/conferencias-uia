# Generated by Django 3.2.3 on 2021-09-06 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presentaciones', '0005_alter_conferencia_password_zoom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencia',
            name='descripcion',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='conferencia',
            name='id_conferencista',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='presentaciones.conferencista'),
        ),
    ]
