# scraper/models.py
from django.db import models

class Property(models.Model):
    property_name = models.CharField(max_length=255)
    property_cost = models.CharField(max_length=255)
    property_type = models.CharField(max_length=255)
    property_area = models.CharField(max_length=255)
    property_locality = models.CharField(max_length=255)
    property_city = models.CharField(max_length=255)
    property_link = models.URLField()
