# Generated by Django 4.0 on 2022-02-05 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.IntegerField(),
        ),
    ]
