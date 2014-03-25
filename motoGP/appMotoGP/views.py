# Create your views here.
from django.template import Context
from django.template.loader import get_template
from appMotoGP.models import *
from django.http import HttpResponse, Http404
from django.views.generic import *
from django.shortcuts import render_to_response


from django.core import serializers

def index(request):
	return render_to_response('indice.html')

def pilotpage(request):

	template = get_template('pilot.html')
	pilots = Pilot.objects.all()
	variables = Context({
		'pilots': pilots
	})
	template_render= template.render(variables)
	return HttpResponse(template_render)

def manufacturerpage(request):

	template = get_template('manufacturer.html')
	manufacturers= Manufacturer.objects.all()
	variables = Context({
		'manufacturers': manufacturers
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

def pilothtmlinfo(request,pilot_id):

	return pilotinfo(request,None,pilot_id)


def pilotinfo(request,format,pilot_id):

	template = get_template('pilotinfo.html')
	try:
		pilot = Pilot.objects.get(id=pilot_id)
	except:
		raise Http404('Pilot not found.')
	if format=='json':

		data = serializers.serialize('json', [pilot,])
		return HttpResponse(data, mimetype='application/json')
	elif format=='xml':

		data = serializers.serialize('xml', [pilot,])
		return HttpResponse(data, mimetype='application/xml')
	else:
		variables = Context({
			'pilot':pilot,
		})
		output = template.render(variables)
		return HttpResponse(output)
		
def manufacturerinfo(request,manufacturer_id):

	template = get_template('manufacturerinfo.html')
	try:
		manufacturer = Manufacturers.objects.get(id=manufacturer_id)
	except:
		raise Http404('Manufacturer not found.')
	variables = Context({
		'manufacturer':manufacturer,
	})
	output = template.render(variables)
	return HttpResponse(output)
