from django import forms
from cclabbooking.models import Zones_Software, Zones_Os

class RequestForm(forms.Form):
    
    date      = forms.DateField()
    start_hour 	  = forms.IntegerField()
    number_of_hours = forms.IntegerField()
    
    #find data structure for the zone
    zone1= forms.BooleanField(initial = False)
    zone2= forms.BooleanField(initial = False)
    zone3= forms.BooleanField(initial = False)
    zone4= forms.BooleanField(initial = False)
    zone5= forms.BooleanField(initial = False)
    zone6= forms.BooleanField(initial = False)

    #other fields
    contact_number = forms.CharField(max_length=15)
    purpose = forms.CharField(max_length=100)

    lan_required = forms.BooleanField(initial = True)
    internet_required = forms.BooleanField(initial = True)

class ZoneOsSelectionForm(forms.Form):
    SOFTWARE_CHOICES = (('eclipse', 'eclipse'),('matlab', 'matlab'))
    OS_CHOICES = (('windows', 'windows'),('linux', 'linux'))

    # for x in Zones.objects.distinct('software_available'):
    #     all_softwares = all_softwares + x.software_available

    # for x in Zones.objects.distinct('os_available'):
    #     all_os = all_os + x.os_available

    requires_systems = forms.IntegerField()
    software_required = forms.ChoiceField(choices = SOFTWARE_CHOICES)
    os_required = forms.ChoiceField(choices = OS_CHOICES)