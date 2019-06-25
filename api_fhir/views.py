from claim.models import ClaimAdmin
from insuree.models import Insuree
from location.models import HealthFacility

from rest_framework import viewsets

from api_fhir.serializers import PatientSerializer, LocationSerializer, ClaimAdminSerializer


class InsureeViewSet(viewsets.ModelViewSet):
    queryset = Insuree.objects.all()
    serializer_class = PatientSerializer


class HFViewSet(viewsets.ModelViewSet):
    queryset = HealthFacility.objects.all()
    serializer_class = LocationSerializer


class ClaimAdminViewSet(viewsets.ModelViewSet):
    queryset = ClaimAdmin.objects.all()
    serializer_class = ClaimAdminSerializer
