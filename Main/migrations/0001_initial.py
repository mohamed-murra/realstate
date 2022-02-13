# Generated by Django 4.0 on 2022-02-05 19:40

import Main.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Acounnt', '0001_initial'),
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
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('building_type', models.CharField(choices=[('أستديو', 'أستديو'), ('عماراة', 'عماراة'), ('ارضي', 'ارضي'), ('مزرعة', 'مزرعة')], max_length=10)),
                ('flour', models.IntegerField(blank=True, null=True)),
                ('num_rooms', models.IntegerField()),
                ('rent_type', models.CharField(blank=True, choices=[('سنة', 'سنة'), ('شهر', 'شهر'), ('أسبوع', 'أسبوع'), ('يوم', 'يوم')], max_length=10, null=True)),
                ('payment_type', models.CharField(choices=[('كاش', 'كاش'), ('تقسيط', 'تقسيط')], max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('space', models.IntegerField()),
                ('slug', models.SlugField(unique=True)),
                ('property_type', models.CharField(choices=[('بيع', 'بيع'), ('أيجار', 'أيجار')], max_length=10)),
                ('bathrooms', models.IntegerField(blank=True, null=True)),
                ('Agent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Agents', to='Acounnt.acount')),
                ('aria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='place', to='Main.aria')),
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
        migrations.AddField(
            model_name='aria',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.city'),
        ),
    ]
