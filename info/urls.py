from django.contrib import admin
from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employer', views.EmployerViewSet, 'employers')
router.register(r'about', views.FairInfoViewSet, 'about')
router.register(r'organizer', views.OrganizerViewSet, 'organizers')
router.register(r'sponsor', views.SponsorViewSet, 'sponsors')
router.register(r'partner', views.PartnerViewSet, 'partners')
router.register(r'mediapartner', views.MediaPartnerViewSet, 'mediapartners')
router.register(r'shedule', views.SheduleViewSet, 'shedules')
urlpatterns = [
    url(r'^', include(router.urls)),
]