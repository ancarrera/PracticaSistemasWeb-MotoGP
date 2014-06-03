from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *


class CountrySerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='appMotoGP:country-detail')
    pilots = HyperlinkedRelatedField(many=True, read_only=True, view_name='appMotoGP:pilotinfohtml')
    manufacturers = HyperlinkedRelatedField(many=True, read_only=True, view_name='appMotoGP:manufacturerinfohtml')
    class Meta:
        model = Country
        fields = ('country_name', 'description')

class PilotSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='appMotoGP:pilotinfohtml')
    class Meta:
        model = Pilot
        fields = ('pilot_name', 'pilot_age', 'race_win', 'representative_company','debut_circuit', 'image', 
        	'manufacturer', 'country')

class ManufacturerSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='appMotoGP:manufacturerinfohtml')
    pilots = HyperlinkedRelatedField(view_name='appMotoGP:pilotinfohtml')
    categories = HyperlinkedRelatedField(view_name='appMotoGP:categoryinfohtml')
    class Meta:
        model = Manufacturer
        fields = ('manufacturer_name', 'country')

class CategorySerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='appMotoGP:categoryinfohtml')
    pilots = HyperlinkedRelatedField(view_name='appMotoGP:pilotinfohtml')
    manufacturers = HyperlinkedRelatedField(view_name='appMotoGP:manufacturerinfohtml')
    class Meta:
        model = Category
        fields = ('name', 'description', 'manufacturer')

class PilotReviewSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='pilotreview-detail')
    pilot = HyperlinkedRelatedField(view_name='pilot-detail')
    user = CharField(read_only=True)
    class Meta:
        model = PilotReview
        fields = ('url', 'rating', 'comment','date','user','pilot')