from appMotoGP.models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class ChangeFirstName(forms.Form):

	firstname = forms.CharField(label="Cambiar nombre")

	class Meta():
		model = User
		fields  = ("firstname")


class ChangePassword(forms.Form):
	password1 = forms.CharField(label="Password",widget=forms.PasswordInput)
	password2 = forms.CharField(label="Repite password",widget=forms.PasswordInput)
	class Meta():
		model = User
		fields=('password1','password2')

class ChangeSecondName(forms.Form):

	secondname = forms.CharField(label="Cambiar Apellidos")

	class Meta():

		model = User
		fields  = ("secondname")

class ChangeEmail(forms.Form):

	email = forms.CharField(label="Cambiar email")

	class Meta():

		model = User
		fields = ("email")

class ChangeUsername(forms.Form):

	username = forms.CharField(label="Nuevo usuario")

	class Meta():
		model = User
		fields = ('username')

class PilotForm(ModelForm):

	class Meta:
		model = Pilot

