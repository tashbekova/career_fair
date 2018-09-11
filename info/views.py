from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
# Create your views here.

from .models import *
from .serializers import *

class FairInfoViewSet(ReadOnlyModelViewSet):
    queryset = FairInfo.objects.all()
    serializer_class = FairInfoSerializer

class OrganizerViewSet(ReadOnlyModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

class SponsorViewSet(ReadOnlyModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

class PartnerViewSet(ReadOnlyModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class EmployerViewSet(ReadOnlyModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class SheduleViewSet(ReadOnlyModelViewSet):
    queryset = Shedule.objects.all()
    serializer_class = SheduleSerializer


