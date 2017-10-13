from django.contrib.gis.db import models

WGS84_SRID = 4326


class TestModel(models.Model):
    location = models.PointField(srid=WGS84_SRID)
