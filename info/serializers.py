from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from .models import *

class FairInfoSerializer(ModelSerializer):
    class Meta:
        model = FairInfo
        fields = '__all__'

class OrganizerSerializer(ModelSerializer):
    class Meta:
        model = Organizer
        fields = '__all__'

class SponsorSerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'

class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

class MediaPartnerSerializer(ModelSerializer):
    class Meta:
        model = MediaPartner
        fields = '__all__'

class EmployerSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


class SheduleSerializer(ModelSerializer):
    class Meta:
        model = Shedule
        fields = '__all__'