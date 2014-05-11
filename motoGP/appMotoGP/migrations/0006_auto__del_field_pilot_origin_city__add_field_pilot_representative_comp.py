# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Pilot.origin_city'
        db.delete_column(u'appMotoGP_pilot', 'origin_city')

        # Adding field 'Pilot.representative_company'
        db.add_column(u'appMotoGP_pilot', 'representative_company',
                      self.gf('django.db.models.fields.CharField')(max_length=60, null=True),
                      keep_default=False)


        # Changing field 'Pilot.debut_circuit'
        db.alter_column(u'appMotoGP_pilot', 'debut_circuit', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

    def backwards(self, orm):
        # Adding field 'Pilot.origin_city'
        db.add_column(u'appMotoGP_pilot', 'origin_city',
                      self.gf('django.db.models.fields.CharField')(default='No value', max_length=60),
                      keep_default=False)

        # Deleting field 'Pilot.representative_company'
        db.delete_column(u'appMotoGP_pilot', 'representative_company')


        # Changing field 'Pilot.debut_circuit'
        db.alter_column(u'appMotoGP_pilot', 'debut_circuit', self.gf('django.db.models.fields.CharField')(max_length=60))

    models = {
        u'appMotoGP.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['appMotoGP.Manufacturer']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'appMotoGP.country': {
            'Meta': {'object_name': 'Country'},
            'country_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'appMotoGP.manufacturer': {
            'Meta': {'object_name': 'Manufacturer'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appMotoGP.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer_name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'appMotoGP.pilot': {
            'Meta': {'object_name': 'Pilot'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appMotoGP.Country']"}),
            'debut_circuit': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appMotoGP.Manufacturer']"}),
            'pilot_age': ('django.db.models.fields.IntegerField', [], {}),
            'pilot_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'race_win': ('django.db.models.fields.IntegerField', [], {}),
            'representative_company': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'})
        }
    }

    complete_apps = ['appMotoGP']