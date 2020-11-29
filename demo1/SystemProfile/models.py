from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class SystemProfile(models.Model):
    systemUser = models.ForeignKey(User, on_delete=models.CASCADE)
    NID = models.CharField(max_length=255, verbose_name='NID',)
    Registration = models.CharField(max_length=255, verbose_name='Registration')
    vehicleType = models.CharField(max_length=255, verbose_name='Type of vehicle')
    vehicleCC = models.CharField(max_length=255, verbose_name='CC of vehicle')
    presentAddress = models.CharField(max_length=255, verbose_name='Present Address')
    permanentAddress = models.CharField(max_length=255, verbose_name='Present Address')
    phone = models.CharField(max_length=255, verbose_name='Phone',)
    occupation = models.CharField(max_length=255, verbose_name='Occupation')
    picture = models.ImageField(max_length=255, verbose_name='Upload photo', upload_to='picture/')
    drivingLicense = models.CharField(max_length=255, verbose_name='driving License Number')