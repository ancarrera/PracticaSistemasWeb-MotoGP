# Create your views here.
from django.template import Context, RequestContext
from django.template.loader import get_template
from appMotoGP.models import *
from django import forms
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import logout

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

def indexhtml(request):

	template = get_template('index.html')
	variables = Context({
			'login_user':getUser(request)
	})

	template_render= template.render(variables)
	return HttpResponse(template_render)



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

#TRATAMIENTO DE USUARIOS

#creamos subclase de UserCreationForm para que nos cree el formulario 
#para el registro
class UserCreateForm(UserCreationForm):
	username = forms.CharField(label="Introduce usuario")
	email = forms.EmailField(label="Introduce un email")
	first_name = forms.CharField(label="Introduce tu nombre")
	second_name = forms.CharField(label="Introduce tus apellidos")
	password1 = forms.CharField(label="Password",widget=forms.PasswordInput)
	password2 = forms.CharField(label="Repite password", widget=forms.PasswordInput)


	class Meta(UserCreationForm.Meta):
		model = User
		fields = ("username","first_name","second_name","email","password1","password2",)

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email=self.cleaned_data["email"]
		user.set_password(self.cleaned_data["password1"])
		user.username = self.cleaned_data["username"]
		user.second_name = self.cleaned_data["second_name"]
		user.first_name = self.cleaned_data["first_name"]
		if commit:
			user.save()
			return user

#crear un nuevo usuario

def newuser(request):
	if request.method=='POST':
		form = UserCreateForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = UserCreateForm()
	return render_to_response('registration/newuser.html',
		   {'form':form},context_instance=RequestContext(request))

#obtener el perfil de usuario

def profileinfo(request):

	template = get_template('userProfile/userprofile.html')
	user=User.objects.get(username__exact=request.user.username)
	user_name = user.username
	user_mail = user.email
	user_first_name = user.first_name
	user_last_name = user.last_name
	variables = Context({
			'user_name':user_name,
			'user_email':user_mail,
			'user_first_name':user_first_name,
			'user_last_name':user_last_name
		})
	output = template.render(variables)
	return HttpResponse(output)



