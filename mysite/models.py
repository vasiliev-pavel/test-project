from django.db import models

# Create your models here.
class Devices(models.Model):
    serial_number = models.IntegerField()
    status_input1 = models.BooleanField()
    status_input2 = models.BooleanField()
    status_output1 = models.BooleanField()
    status_output2 = models.BooleanField()
    voltage = models.IntegerField()
    temperature = models.IntegerField()