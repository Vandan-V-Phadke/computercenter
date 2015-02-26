from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Slide(models.Model):
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='lcd/images/', height_field="height", width_field="width")
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
