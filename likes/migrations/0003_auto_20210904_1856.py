# Generated by Django 3.2.3 on 2021-09-04 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0002_alter_like_cartel'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartel',
            name='dia',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartel',
            name='sala',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
