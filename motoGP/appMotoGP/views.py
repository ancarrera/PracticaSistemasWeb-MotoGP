# Create your views here.
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
from appMotoGP.models import *

def pilotpage(request):

	template = get_template('pilot.html')
	pilots = Pilot.objects.all()
	variables = Context({
		'pilots': pilots
	})
	template_render= template.render(variables)
	return HttpResponse(template_render)

def manofacturerpage(request):

	template = get_template('manofacturer.html')
	manofacturers= Manofacturer.objects.all()
	variables = Context({
		'manofacturers': manofacturers
	})
	template_render = template.render(variables)
	return HttpResponse(template_render)