from django.db import models


class Country(models.Model):

	country_name = models.CharField(max_length=40)
	description = models.CharField(max_length=2000)
	def __unicode__(self):
		return self.country_name

class Manufacturer(models.Model):

	manufacturer_name = models.CharField(max_length=40)
	country = models.ForeignKey(Country)
	def __unicode__(self):
		return self.manufacturer_name

class Pilot(models.Model):

	pilot_name = models.CharField(max_length=40)
	pilot_age = models.IntegerField()
	race_win = models.IntegerField()
	manufacturer = models.ForeignKey(Manufacturer)
	country = models.ForeignKey(Country)
	def __unicode__(self):
		return self.pilot_name +"-"+ str(self.pilot_age)+"anyos"


class Category(models.Model):

	name = models.CharField(max_length=40)
	description = models.CharField(max_length=2000)
	manufacturer = models.ManyToManyField(Manufacturer)
	def __unicode__(self):
		return self.name


