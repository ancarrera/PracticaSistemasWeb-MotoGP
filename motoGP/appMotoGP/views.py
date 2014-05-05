# Create your views here.
from django.template import Context, RequestContext
from django.template.loader import get_template
from django import forms
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from django.contrib.auth.views import logout
from django.views.generic.edit import CreateView
from appMotoGP.models import *
from django.forms import ModelForm
from rest_framework import generics, permissions



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

@login_required(login_url='/login/')
def indexhtml(request):

	template = get_template('index.html')
	groups = request.user.groups.all()
	variables = Context({
			'login_user':getUser(request),
			'user':request.user,
			'groups': groups
	})

	template_render= template.render(variables)
	return HttpResponse(template_render)


@login_required(login_url='/login/')
def pilotpagehtml(request):

	return pilotpage(request, None)

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def pilotinfohtml(request,pilot_id):

	return pilotinfo(request,None,pilot_id)

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def manufacturerpagehtml(request):

	return manufacturerpage(request, None)

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def manufacturerinfohtml(request,manufacturer_id):

	return manufacturerinfo(request,None,manufacturer_id)

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def countrypagehtml(request):

	return countrypage(request, None)

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def countryinfohtml(request,country_id):

	return countryinfo(request,None,country_id)

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def categorypagehtml(request):

	return categorypage(request, None)

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def categoryinfohtml(request,category_id):

	return categoryinfo(request,None,category_id)

@login_required(login_url='/login/')
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
	first_name = forms.CharField(label="Introduce tu nombre")
	last_name = forms.CharField(label="Introduce tus apellidos")
	email = forms.EmailField(label="Introduce un email")
	password1 = forms.CharField(label="Password",widget=forms.PasswordInput)
	password2 = forms.CharField(label="Repite password", widget=forms.PasswordInput)


	class Meta(UserCreationForm.Meta):
		model = User
		fields = ("username","first_name","last_name","email","password1","password2",)

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email=self.cleaned_data["email"]
		user.set_password(self.cleaned_data["password1"])
		user.username = self.cleaned_data["username"]
		user.last_name = self.cleaned_data["last_name"]
		user.first_name = self.cleaned_data["first_name"]
		if commit:
			user.save()
			return user


#crear un nuevo usuario
@login_required(login_url='/login/')
def newuser(request):
	if request.method=='POST':
		form = UserCreateForm(request.POST)
		if form.is_valid():
			user = form.save()
			if request.user.is_superuser:
				addUserPermissions(user)
			return HttpResponseRedirect('/index/')
	else:
		form = UserCreateForm()
	return render_to_response('registration/newuser.html',
		   {'form':form},context_instance=RequestContext(request))

#obtener el perfil de usuario
def addUserPermissions(specialUser):
	group = Group.objects.get(name='special_user')
	specialUser.groups.add(group)

@login_required(login_url='/login/')
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
			'user_last_name':user_last_name,
		})
	output = template.render(variables)
	return HttpResponse(output)

class ChangePassword(forms.Form):
	password1 = forms.CharField(label="Password",widget=forms.PasswordInput)
	password2 = forms.CharField(label="Repite password",widget=forms.PasswordInput)
	class Meta():
		model = User
		fields=('password1','password2')

@login_required(login_url='/login/')
def changepassword(request):

	if request.method == 'GET':
		form = ChangePassword()
	else:
		form = ChangePassword(request.POST)
		if form.is_valid():			
			user = User.objects.get(username=request.user.username)
			password = form.cleaned_data['password1']
			user.set_password(password)
			user.save(update_fields=['password'])
			return HttpResponseRedirect("/user_profile/")
	return render_to_response('userProfile/change_password.html',{'form':form},context_instance=RequestContext(request))


class ChangeUsername(forms.Form):

	username = forms.CharField(label="Nuevo usuario")

	class Meta():
		model = User
		fields = ('username')


@login_required(login_url='/login/')
def changeusername(request):

	if request.method == 'GET':
		form = ChangeUsername()
	else:
		form = ChangeUsername(request.POST)
		if form.is_valid():			
			user = User.objects.get(username=request.user.username)
			user.username = form.cleaned_data['username']
			user.save(update_fields=['username'])
			return HttpResponseRedirect("/user_profile/")
	return render_to_response('userProfile/change_username.html',{'form':form},context_instance=RequestContext(request))


class ChangeFirstName(forms.Form):

	firstname = forms.CharField(label="Cambiar nombre")

	class Meta():
		model = User
		fields  = ("firstname")

@login_required(login_url='/login/')
def changefirstname(request):

	if request.method == 'GET':
		form = ChangeFirstName()
	else:
		form = ChangeFirstName(request.POST)
		if form.is_valid():			
			user = User.objects.get(username=request.user.username)
			user.first_name = form.cleaned_data['firstname']
			user.save(update_fields=['first_name'])
			return HttpResponseRedirect("/user_profile/")
	return render_to_response('userProfile/change_firstname.html',{'form':form},context_instance=RequestContext(request))

class ChangeSecondName(forms.Form):

	secondname = forms.CharField(label="Cambiar Apellidos")

	class Meta():

		model = User
		fields  = ("secondname")

@login_required(login_url='/login/')
def changesecondname(request):

	if request.method == 'GET':
		form = ChangeSecondName()
	else:
		form = ChangeSecondName(request.POST)
		if form.is_valid():			
			user = User.objects.get(username=request.user.username)
			user.last_name = form.cleaned_data['secondname']
			user.save(update_fields=['last_name'])
			return HttpResponseRedirect("/user_profile/")
	return render_to_response('userProfile/change_secondname.html',{'form':form},context_instance=RequestContext(request))

class ChangeEmail(forms.Form):

	email = forms.CharField(label="Cambiar email")

	class Meta():

		model = User
		fields = ("email")

@login_required(login_url='/login/')
def changeemail(request):

	if request.method == 'GET':
		form = ChangeEmail()
	else:
		form = ChangeEmail(request.POST)
		if form.is_valid():			
			user = User.objects.get(username=request.user.username)
			user.email = form.cleaned_data['email']
			user.save(update_fields=['email'])
			return HttpResponseRedirect("/user_profile/")
	return render_to_response('userProfile/change_email.html',
							{'form':form},context_instance=RequestContext(request))
class PilotForm(ModelForm):

	class Meta:
		model = Pilot

class CreatePilot(CreateView):

	model = Pilot
	template_name = 'management/createpilot.html'
	form_class = PilotForm
	success_url="/pilot"

	def form_valid(self, form):
		return super(CreatePilot, self).form_valid(form)


