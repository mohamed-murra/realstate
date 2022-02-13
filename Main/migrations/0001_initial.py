# Generated by Django 4.0.2 on 2022-02-13 16:07

import Main.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='aria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('messaage', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('flour', models.IntegerField(blank=True, null=True)),
                ('num_rooms', models.IntegerField()),
                ('rent_type', models.CharField(blank=True, choices=[('سنة', 'سنة'), ('شهر', 'شهر'), ('أسبوع', 'أسبوع'), ('يوم', 'يوم')], max_length=10, null=True)),
                ('payment_type', models.CharField(choices=[('كاش', 'كاش'), ('تقسيط', 'تقسيط')], max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('space', models.IntegerField()),
                ('slug', models.SlugField(unique=True)),
                ('status', models.BooleanField(default=True)),
                ('cover', models.ImageField(upload_to=Main.models.uplaod_lucationn)),
                ('property_type', models.CharField(choices=[('للبيع', 'للبيع'), ('للأيجار', 'للأيجار')], max_length=10)),
                ('bathrooms', models.IntegerField(blank=True, null=True)),
                ('Agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('aria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='place', to='Main.aria')),
                ('building_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.building')),
            ],
        ),
        migrations.CreateModel(
            name='galary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=Main.models.uplaod_lucation)),
                ('proper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.house')),
            ],
        ),
        migrations.CreateModel(
            name='extras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('proper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.house')),
            ],
        ),
        migrations.AddField(
            model_name='aria',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.city'),
        ),
    ]
