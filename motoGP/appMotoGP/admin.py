from django.contrib import admin

from appMotoGP.models import Country
from appMotoGP.models import Manufacturer
from appMotoGP.models import Pilot
from appMotoGP.models import Category


admin.site.register(Country) 
admin.site.register(Manufacturer) 
admin.site.register(Pilot) 
admin.site.register(Category) 