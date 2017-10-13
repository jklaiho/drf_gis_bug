from rest_framework import viewsets
from rest_framework_gis import serializers as gis_serializers

from .models import TestModel


class TestModelSerializer(gis_serializers.GeoFeatureModelSerializer):
    class Meta:
        model = TestModel
        geo_field = 'location'
        fields = ('location',)


class TestModelViewSet(viewsets.ModelViewSet):
    serializer_class = TestModelSerializer
    queryset = TestModel.objects.all()
