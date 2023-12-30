from django.db import models
from utils.models import BaseModel


# Create your models here.
class Region(BaseModel):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"


class District(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"
