# Create your views here.
from django.template import Context
from django.template.loader import get_template
from appMotoGP.models import *
from django.http import HttpResponse, Http404
from django.views.generic import *

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

def countrypage(request):
	template = get_template('country.html')
	countries= Country.objects.all()
	variables = Context({
		'countries': countries
	})
	template_render = template.render(variables)
	return HttpResponse(template_render)

def categorypage(request):

	template = get_template('category.html')
	categories = Category.objects.all()
	variables = Context({
		'categories': categories
	})
	template_render = template.render(variables)
	return HttpResponse(template_render)

def pilotinfo(request,pilot_id):

	template = get_template('pilotinfo.html')
	try:
		pilot = Pilot.objects.get(id=pilot_id)
	except:
		raise Http404('Pilot not found.')
	variables = Context({
		'pilot':pilot,
	})
	output = template.render(variables)
	return render(request, 'templates/pilotinfo.html',{"pilot":pilot},content_type="application/json+xml")

def manufacturerinfo(request,manufacturer_id):

	template = get_template('manufacturerinfo.html')
	try:
		manufacturer = Manofacturers.objects.get(id=manufacturer_id)
	except:
		raise Http404('Manufacturer not found.')
	variables = Context({
		'manufacturer':manufacturer,
	})
	output = template.render(variables)
	return HttpResponse(output)
