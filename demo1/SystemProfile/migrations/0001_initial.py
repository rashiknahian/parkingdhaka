# Generated by Django 3.1.3 on 2020-11-28 18:14

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
            name='SystemProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NID', models.CharField(max_length=255, verbose_name='NID')),
                ('Registration', models.CharField(max_length=255, verbose_name='Registration')),
                ('vehicleType', models.CharField(max_length=255, verbose_name='Type of vehicle')),
                ('vehicleCC', models.CharField(max_length=255, verbose_name='CC of vehicle')),
                ('presentAddress', models.CharField(max_length=255, verbose_name='Present Address')),
                ('permanentAddress', models.CharField(max_length=255, verbose_name='Present Address')),
                ('phone', models.CharField(max_length=255, verbose_name='Phone')),
                ('occupation', models.CharField(max_length=255, verbose_name='Occupation')),
                ('picture', models.ImageField(max_length=255, upload_to='picture/', verbose_name='Upload photo')),
                ('drivingLicense', models.CharField(max_length=255, verbose_name='driving License Number')),
                ('systemUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]