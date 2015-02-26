from django.db import models


class BookingRequest(models.Model):
    user_id = models.CharField(max_length=25)
    time_of_request = models.DateTimeField(auto_now_add=True)
    date_of_booking = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    ac_required = models.NullBooleanField(default=None, blank=True, null=True)
    projector_required = models.NullBooleanField(default=None, blank=True, null=True)
    pa_required = models.NullBooleanField(default=None, blank=True, null=True)
    purpose = models.CharField(max_length=200)
    csa_confirmed = models.NullBooleanField(default=None, blank=True, null=True)
    backstage_confirmed = models.NullBooleanField(default=None, blank=True, null=True)
    swd_incharge_confirmed = models.NullBooleanField(default=None, blank=True, null=True)
    audi_incharge_confirmed = models.NullBooleanField(default=None, blank=True, null=True)
    asset_manager_confirmed = models.NullBooleanField(default=None, blank=True, null=True)
    uuid_csa = models.CharField(max_length=40)
    uuid_backstage = models.CharField(max_length=40)
    uuid_swd = models.CharField(max_length=40)
    uuid_audi = models.CharField(max_length=40)
    uuid_asset = models.CharField(max_length=40)