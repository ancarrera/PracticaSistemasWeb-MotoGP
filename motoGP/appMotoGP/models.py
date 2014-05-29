from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.urlresolvers import reverse

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
	representative_company = models.CharField(max_length=60, null=True)
	debut_circuit = models.CharField(max_length=60, null=True)
	image = models.ImageField(upload_to='img', null=True, blank=True, default='img/no-image.png')
	manufacturer = models.ForeignKey(Manufacturer)
	country = models.ForeignKey(Country)
	creator = models.CharField(max_length=60, null=True)

	def __unicode__(self):
		return u"%s" % self.pilot_name

	def get_absolute_url(self):
		return reverse('pilot_detail', kwargs={'pk': self.pk})

	def totalRating(self):
		currentRating = 0.0
		for rew in self.pilotreview_set.all():
			currentRating += rew.rating
		totalreviews = self.pilotreview_set.count()
		return currentRating / totalreviews

class Category(models.Model):

	name = models.CharField(max_length=40)
	description = models.CharField(max_length=2000)
	manufacturer = models.ManyToManyField(Manufacturer)
	def __unicode__(self):
		return self.name

def getSuperuser():
	return User.objects.get(pk=1)

class Review(models.Model):

    RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=getSuperuser)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class PilotReview(Review):
    pilot = models.ForeignKey(Pilot)

    def __unicode__(self):
		return "comentario-" + self.user.username+"-"+str(self.date)


