from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(FairInfo)
admin.site.register(Organizer)
admin.site.register(Sponsor)
admin.site.register(Partner)
admin.site.register(Employer)
admin.site.register(Shedule)
admin.site.register(CompanyType)