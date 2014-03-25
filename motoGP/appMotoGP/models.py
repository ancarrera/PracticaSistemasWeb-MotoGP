from django.db import models


class Country(models.Model):

	country_name = models.CharField(max_length=40)
	def __unicode__(self):
		return self.country_name

class Manofacturer(models.Model):

	manofacturer_name = models.CharField(max_length=40)
	country = models.ForeignKey(Country)
	def __unicode__(self):
		return self.manofacturer_name

class Pilot(models.Model):

	pilot_name = models.CharField(max_length=40)
	pilot_age = models.IntegerField()
	race_win = models.IntegerField()
	manofacturer = models.ForeignKey(Manofacturer)
	country = models.ForeignKey(Country)
	def __unicode__(self):
		return self.pilot_name +" "+ str(self.pilot_age)


class Category(models.Model):

	name = models.CharField(max_length=40)
	manofacturer = models.ManyToManyField(Manofacturer)
	def __unicode__(self):
		return self.name


