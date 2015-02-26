from django.shortcuts import render
from cclabbooking.forms import ZoneOsSelectionForm, RequestForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from cclabbooking.models import Zones_Software, Zones_Os, Request
from django.utils.datetime_safe import datetime
from django.views.decorators.csrf import csrf_exempt
from django.template import loader, RequestContext
import json

# Create your views here.
@csrf_exempt
def new_request(request):
    response_data = {}
    #write all and conditions here
    if ('date' in request.POST):
        req_date = request.POST.get('date')
        start_time = request.POST.get('start_hour')
        hours = request.POST.get('no_of_hours',False)
        
        #get individual zones status from request
        zoner1 = int(request.POST.get('zone1'))
        zoner2 = int(request.POST.get('zone2'))
        zoner3 = int(request.POST.get('zone3'))
        zoner4 = int(request.POST.get('zone4'))
        zoner5 = int(request.POST.get('zone5'))
        zoner6 = int(request.POST.get('zone6'))

        contact_number = request.POST.get('contact')
        purpose = request.POST.get('purpose')
        software = request.POST.get('software')
        lan = request.POST.get('lan')
        internet = request.POST.get('internet')

        #write this data to database
        new_request = Request(date = req_date, start_hour = start_time, no_of_hours = hours, user = "Test User", 
            zone1 = zoner1, zone2 = zoner2, zone3 = zoner3, zone4 = zoner4, zone5 = zoner5, zone6 = zoner6, lan_required = lan, 
            internet_required = internet, status = False, contact_number = contact_number, softwares = software, os= purpose )

        new_request.save()

        response_data['result'] = 'success'

    else:
        response_data['result'] = 'failure'


    return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


#view called in initial form which selects zones based on the os and the requirement
def selectzone(request):
    if request.method == 'POST':
        # A POST request: Handle Form Upload
        form = ZoneOsSelectionForm(request.POST) 
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            os = form.cleaned_data['os_required']
            software = form.cleaned_data['software_required']
            #analyse which zones can be given for the request
            zone = []
            for x in Zones_Os.objects.all():
            	if (os == x.os_available):
            		zone.append(x.zone_number)

            return render(request, 'show_zones.html', {'zones' : zone })

    else:
        form = ZoneOsSelectionForm()

    return render(request, 'request_form.html', {'form': form,})

@csrf_exempt
def show_availability(request):
    #get all entries for the given date
    if (('year' in request.POST) and ('month' in request.POST) and ('day' in request.POST)):
        year = request.POST.get('year')
        month = request.POST.get('month')
        day = request.POST.get('day')

        request_date = datetime(year = int(year) , month = int(month) , day = int(day)) 

        #main availability list
        availability_list = []
        response_data = {}

        for x in Request.objects.filter(date = request_date):
            start_hour = x.start_hour
            no_of_hours = x.no_of_hours 
            
            zone1 = x.zone1
            zone2 = x.zone2
            zone3 = x.zone3
            zone4 = x.zone4
            zone5 = x.zone5
            zone6 = x.zone6

            #construct individual lists for each entry
            for i in range(start_hour, start_hour + no_of_hours):     
                request_list = []
                request_list.append(i)
                request_list.append(zone1)
                request_list.append(zone2)
                request_list.append(zone3)
                request_list.append(zone4)
                request_list.append(zone5)
                request_list.append(zone6)
                availability_list.append(request_list)

        response_data['result'] = 'success'
        response_data['data'] = availability_list

    else:
        response_data['result'] = 'failure'


    return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
        
    

def admin_view(request):

    pending_requests = []
    #if(request.user.is_staff):
    for request1 in Request.objects.filter(status = False):
        pending_request = []
        pending_request.append(request1.user)
        pending_request.append(request1.date)
        pending_request.append(request1.start_hour)
        pending_request.append(request1.no_of_hours)
        pending_request.append(request1.zone1)
        pending_request.append(request1.zone2)
        pending_request.append(request1.zone3)
        pending_request.append(request1.zone4)
        pending_request.append(request1.zone5)
        pending_request.append(request1.zone6)

        #add list of single request to main list
        pending_requests.append(pending_request)

    return render(request, 'adminview.html', {'requests1' : pending_requests})