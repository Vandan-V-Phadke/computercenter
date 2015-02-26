import json
import uuid
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from .models import BookingRequest


def home(request):
    return HttpResponse("SAf")


mail_body_text = """
Hello,

There is a new booking request for the auditorium. Following are the details for the same.

Requested by: %s
Date: %s
From: %s
To: %s
purpose: %s
AC required: %s
Projector required: %s
PA System required: %s

Please click the following link to grant the permission.

%s

--------------- 
Computer Center
"""

mail_body_html = """
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
    </body>
</html>

"""


@csrf_exempt
def book(request):
    if request.method == 'POST':
        # Validating request
        if (#'user_id' in request.POST and
            'date_of_booking' in request.POST and
            'start_time' in request.POST and
            'end_time' in request.POST and
            'ac_required' in request.POST and
            'projector_required' in request.POST and
            'pa_required' in request.POST,
            'purpose' in request.POST):
            user_id = 'f2012470@goa.bits-pilani.ac.in'#request.POST.get('user_id')
            date_of_booking = request.POST.get('date_of_booking')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            ac_required = request.POST.get('ac_required')
            projector_required = request.POST.get('projector_required')
            pa_required = request.POST.get('pa_required')
            purpose = request.POST.get('purpose')

            # Validating availability
            temp = start_time.split(":")
            start_time_datetime =  datetime.time(int(temp[0]), int(temp[1]))
            clash = False
            booking_for_days = BookingRequest.objects.filter(date_of_booking='2015-01-28')
            for i in booking_for_days:
                if start_time_datetime >= i.start_time and start_time_datetime < i.end_time:
                    clash = True
            
            if clash:
                return HttpResponse('not available')

            # Generating security codes
            uuid_csa = uuid.uuid4().get_hex()
            uuid_backstage = uuid.uuid4().get_hex()
            uuid_swd = uuid.uuid4().get_hex()
            uuid_audi = uuid.uuid4().get_hex()
            uuid_asset = uuid.uuid4().get_hex()

            # Saving request in database
            booking_request = BookingRequest(user_id=user_id,
                                             date_of_booking=date_of_booking,
                                             start_time=start_time,
                                             end_time=end_time,
                                             ac_required=ac_required,
                                             projector_required=projector_required,
                                             pa_required=pa_required,
                                             purpose=purpose,
                                             uuid_csa=uuid_csa,
                                             uuid_backstage=uuid_backstage,
                                             uuid_swd=uuid_swd,
                                             uuid_audi=uuid_audi,
                                             uuid_asset=uuid_asset)
            booking_request.save()
            # Sending emails
            send_mail('New Auditorium booking request',
                'Here is the message.',
                settings.EMAIL_HOST_USER,
                ['mrsud94@gmail.com'],
                fail_silently=False
            )
            return HttpResponse('successful')
        else:
            return HttpResponse('incomplete details', status=200)

