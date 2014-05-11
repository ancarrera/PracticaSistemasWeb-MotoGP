from appMotoGP.models import *
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import Context, RequestContext

from forms import *
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