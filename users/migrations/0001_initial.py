# Generated by Django 3.2.6 on 2021-09-20 09:16

import datetime
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
            name='Drive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drive_name', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('target', models.IntegerField()),
                ('desc', models.CharField(default='', max_length=200)),
                ('host', models.ManyToManyField(related_name='hostedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(default='', max_length=100, null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2021, 9, 20, 14, 46, 35, 722759))),
                ('image', models.ImageField(upload_to='images')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('drive', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.drive')),
            ],
        ),
        migrations.CreateModel(
            name='Planter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drive_participated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inDrives', to='users.drive')),
                ('planter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='plantedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]