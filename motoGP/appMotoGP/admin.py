from django.contrib import admin

from appMotoGP.models import *

admin.site.register(Country) 
admin.site.register(Manufacturer) 
admin.site.register(Pilot) 
admin.site.register(Category)
admin.site.register(PilotReview)