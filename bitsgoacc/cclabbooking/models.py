from django.db import models

# Create your models here. 
class Request(models.Model):

    date = models.DateField()
    start_hour 	  = models.IntegerField()
    no_of_hours = models.IntegerField()
    user = models.CharField(max_length = 30)
    contact_number = models.CharField(max_length=15)
    softwares = models.CharField(max_length=100)
    os = models.CharField(max_length=20)
    
    zone1 = models.BooleanField(default = True)
    zone2 = models.BooleanField(default = True)
    zone3 = models.BooleanField(default = True)
    zone4 = models.BooleanField(default = True)
    zone5 = models.BooleanField(default = True)
    zone6 = models.BooleanField(default = True)

    lan_required = models.BooleanField(default = True)
    internet_required = models.BooleanField(default = True)
    status = models.BooleanField(default = False)

    def __str__(self):
        return "Request by " + self.user ;

    class Meta:
        ordering = ['date']

#one to many table (1 zone can have many softwares or OS)
class Zones_Software(models.Model):
    zone_number = models.IntegerField()
    software_available = models.CharField(max_length = 30)
    
class Zones_Os(models.Model):
    zone_number = models.IntegerField()
    os_available = models.CharField(max_length = 10)
