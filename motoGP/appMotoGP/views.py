# Create your views here.

from django.core import serializers
from django.views.generic import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import logout
from django.views.generic.edit import CreateView,UpdateView
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from django.core import urlresolvers


from serializers import *
from userviews import *



def welcomeindex(request):
	template = get_template('index_welcome.html')
	variables = Context({
			'titlehead': 'MotoGP application',        
			'pagetitle': 'Bienvenido a MotoGP',
			'user':getUser(request)
	})
	template_render= template.render(variables)
	return HttpResponse(template_render)

def getUser(request):

	if request.user.is_authenticated():
		return request.user.username
	else:
		return 'anonimo'

def login(request):
	return render_to_response('registration/login.html')

@login_required(login_url='/accounts/login/')
def indexhtml(request):

	template = get_template('index.html')
	group = checkEspecialUserGroup(request.user)
	variables = Context({
			'login_user':getUser(request),
			'user':request.user,
			'group':group,
			'special_user_head':'Apartado para usuarios con permisos especiales'
	})

	template_render= template.render(variables)
	return HttpResponse(template_render)


def checkEspecialUserGroup(user):

	group_especial_user = None
	for group in user.groups.all():
		if group.name == 'special_user':
			group_especial_user = group

	return group_especial_user


def createSerializerList(pilot_list, user, group):

	serializer_list = pilot_list
	serializer_list.append(user)
	if group != None:
		serializer_list.append(group)
	return serializer_list


@login_required(login_url='/accounts/login/')
def pilotpagehtml(request):

	return pilotpage(request, None)

@login_required(login_url='/accounts/login/')
def pilotpage(request,format):

	template = get_template('pilot.html')
	pilot_list = []
	
	for pilot in Pilot.objects.all():
		pilot_list.append(pilot)

	user= User.objects.get(username=request.user.username)
	group = checkEspecialUserGroup(user)

	if format=='json':

		serializer_list = createSerializerList(pilot_list,user,group)
		data = serializers.serialize('json',serializer_list)
		return HttpResponse(data, mimetype='application/json')

	elif format=='xml':
		
		serializer_list = createSerializerList(pilot_list,user,group)
		data = serializers.serialize('xml',serializer_list)

		return HttpResponse(data, mimetype='application/xml')
	else:
		variables = Context({
			'pilots': pilot_list,
			'user': user,
			'group':group

			
		})
		template_render= template.render(variables)
		return HttpResponse(template_render)

@login_required(login_url='/accounts/login/')
def pilotinfohtml(request,pilot_id):

	return pilotinfo(request,None,pilot_id)

@login_required(login_url='/accounts/login/')
def pilotinfo(request,format,pilot_id):

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
			'rating':Review.RATING_CHOICES
		})
		return render_to_response('pilotinfo.html',variables,context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def manufacturerpagehtml(request):

	return manufacturerpage(request, None)

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def manufacturerinfohtml(request,manufacturer_id):

	return manufacturerinfo(request,None,manufacturer_id)

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def countrypagehtml(request):

	return countrypage(request, None)

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def countryinfohtml(request,country_id):

	return countryinfo(request,None,country_id)

@login_required(login_url='/accounts/login/')
def countryinfo(request,format,country_id):

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

@login_required(login_url='/accounts/login/')
def categorypagehtml(request):

	return categorypage(request, None)

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def categoryinfohtml(request,category_id):

	return categoryinfo(request,None,category_id)

@login_required(login_url='/accounts/login/')
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


class CreatePilot(CreateView):

	model = Pilot
	template_name = 'management/createpilot.html'
	form_class = PilotForm
	success_url="/pilots"

	def get_initial(self):

		default_creator = "Created by "+self.request.user.username
		initial={'creator':default_creator,}
		return initial

	def form_valid(self, form):
		return super(CreatePilot, self).form_valid(form)

class UpdatePilot(UpdateView):

	model = Pilot
	template_name = 'management/modifyPilot.html'
	form_class = PilotFormMod
	success_url="/pilots"

	def get_initial(self):
		pk=self.kwargs['pk']
		pilot = Pilot.objects.get(pk=pk)
		initial={'pilot_name':pilot.pilot_name,
			   'pilot_age':pilot.pilot_age,'race_win':pilot.race_win,'manufacturer':pilot.manufacturer,
			    'country':pilot.country,}
		return initial

	def form_valid(self, form):
		return super(UpdatePilot, self).form_valid(form)


@login_required(login_url='/accounts/login/')
def review(request, pk):
	pilot = get_object_or_404(Pilot, pk=pk)

	new_review = PilotReview(
		rating=request.POST['rating'],
		comment=request.POST['comment'],
		user=request.user,
		pilot=pilot)
	new_review.save()
	return HttpResponseRedirect(urlresolvers.reverse('pilot_detail', args=(pilot.id,)))



#API RESTful

class APICountryList(generics.ListCreateAPIView):
    model = Country
    serializer_class = CountrySerializer

class APICountryDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Country
    serializer_class = CountrySerializer

class APIPilotList(generics.ListCreateAPIView):
    model = Pilot
    serializer_class = PilotSerializer

class APIPilotDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Pilot
    serializer_class = PilotSerializer

class APICategoryList(generics.ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer

class APICategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Category
    serializer_class = CategorySerializer

class APIManufacturerList(generics.ListCreateAPIView):
    model = Manufacturer
    serializer_class = ManufacturerSerializer

class APIManufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Manufacturer
    serializer_class = ManufacturerSerializer

class APIPilotReviewList(generics.ListCreateAPIView):
    model = PilotReview
    serializer_class = PilotReviewSerializer
    
class APIPilotReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    model = PilotReview
    serializer_class = PilotReviewSerializer

