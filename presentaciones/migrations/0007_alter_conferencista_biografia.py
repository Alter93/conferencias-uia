# Generated by Django 3.2.6 on 2021-09-06 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentaciones', '0006_auto_20210906_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencista',
            name='biografia',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
