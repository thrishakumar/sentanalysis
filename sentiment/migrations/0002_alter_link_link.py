# Generated by Django 3.2.9 on 2021-12-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link',
            field=models.URLField(),
        ),
    ]
