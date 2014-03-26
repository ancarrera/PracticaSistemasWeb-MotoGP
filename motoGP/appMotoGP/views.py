# Create your views here.
from django.template import Context
from django.template.loader import get_template
from appMotoGP.models import *
from django.http import HttpResponse, Http404
from django.views.generic import *
from django.shortcuts import render_to_response,render

from django.core import serializers

def indexhtml(request):
	#return render_to_response(request, 'motoGP/templates/index.html',
        #content_type="application/xml")
	return render_to_response('index.html')
#def index(request, format):


def pilotpagehtml(request):

	return pilotpage(request, None)


def pilotpage(request,format):

	template = get_template('pilot.html')
	pilots = Pilot.objects.all()
	if format=='json':
		data = serializers.serialize('json', pilots)
		return HttpResponse(data, mimetype='application/json')

	elif format=='xml':
		data = serializers.serialize('xml', pilots)
		return HttpResponse(data, mimetype='application/xml')
	else:
		variables = Context({
			'pilots': pilots
		})
		template_render= template.render(variables)
		return HttpResponse(template_render)


def pilotinfohtml(request,pilot_id):

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


def manufacturerpagehtml(request):

	return manufacturerpage(request, None)


def manufacturerpage(request,format):

	template = get_template('manufacturer.html')
	manufacturers= Manufacturer.objects.all()
	if format=='json':
		data = serializers.serialize('json', manufacturers)
		return HttpResponse(data, mimetype='application/json')

	elif format=='xml':
		data = serializers.serialize('xml', manufacturers)
		return HttpResponse(data, mimetype='application/xml')
	else:
		variables = Context({
		'manufacturers': manufacturers
		})
		template_render = template.render(variables)
		return HttpResponse(template_render)


def manufacturerinfohtml(request,manufacturer_id):

	return manufacturerinfo(request,None,manufacturer_id)


def manufacturerinfo(request,format,manufacturer_id):

	template = get_template('manufacturerinfo.html')
	try:
		manufacturer = Manufacturer.objects.get(id=manufacturer_id)
	except:
		raise Http404('Manufacturer not found.')
	if format=='json':

		data = serializers.serialize('json', [manufacturer,])
		return HttpResponse(data, mimetype='application/json')
	elif format=='xml':

		data = serializers.serialize('xml', [manufacturer,])
		return HttpResponse(data, mimetype='application/xml')
	else:
		variables = Context({
		'manufacturer':manufacturer,
		})
		output = template.render(variables)
		return HttpResponse(output)


def countrypagehtml(request):

	return countrypage(request, None)


def countrypage(request,format):

	template = get_template('country.html')
	countries= Country.objects.all()
	if format=='json':
		data = serializers.serialize('json', countries)
		return HttpResponse(data, mimetype='application/json')

	elif format=='xml':
		data = serializers.serialize('xml', countries)
		return HttpResponse(data, mimetype='application/xml')
	else:
		variables = Context({
		'countries': countries
		})
		template_render = template.render(variables)
		return HttpResponse(template_render)


def countryinfohtml(request,country_id):

	return countryinfo(request,None,country_id)


def countryinfo(request,form,country_id):

	template = get_template('countryinfo.html')
	try:
		country = Country.objects.get(id=country_id)
	except:
		raise Http404('Country not found.')
	if format=='json':

		data = serializers.serialize('json', [country,])
		return HttpResponse(data, mimetype='application/json')
	elif format=='xml':

		data = serializers.serialize('xml', [country,])
		return HttpResponse(data, mimetype='application/xml')
	else:
		variables = Context({
			'country':country,
		})
		output = template.render(variables)
		return HttpResponse(output)


def categorypagehtml(request):

	return categorypage(request, None)


def categorypage(request,format):

	template = get_template('category.html')
	categories = Category.objects.all()
	if format=='json':
		data = serializers.serialize('json', categories)
		return HttpResponse(data, mimetype='application/json')

	elif format=='xml':
		data = serializers.serialize('xml', categories)
		return HttpResponse(data, mimetype='application/xml')
	else:
		
		variables = Context({
		'categories': categories
		})
		template_render = template.render(variables)
		return HttpResponse(template_render)


def categoryinfohtml(request,category_id):

	return categoryinfo(request,None,category_id)

def categoryinfo(request,form,category_id):

	template = get_template('categoryinfo.html')
	try:
		category = Category.objects.get(id=category_id)
	except:
		raise Http404('Category not found.')

	if format=='json':

		data = serializers.serialize('json', [pilot,])
		return HttpResponse(data, mimetype='application/json')
	elif format=='xml':

		data = serializers.serialize('xml', [pilot,])
		return HttpResponse(data, mimetype='application/xml')
	else:
		variables = Context({
			'category':category,
		})
		output = template.render(variables)
		return HttpResponse(output)




