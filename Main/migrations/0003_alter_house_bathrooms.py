# Generated by Django 4.0 on 2022-02-21 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_alter_house_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='bathrooms',
            field=models.IntegerField(),
        ),
    ]
