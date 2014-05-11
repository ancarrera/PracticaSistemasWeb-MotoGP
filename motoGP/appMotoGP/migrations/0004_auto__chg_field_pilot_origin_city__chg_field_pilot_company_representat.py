# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Pilot.origin_city'
        db.alter_column(u'appMotoGP_pilot', 'origin_city', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Pilot.company_representative'
        db.alter_column(u'appMotoGP_pilot', 'company_representative', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'Pilot.origin_city'
        db.alter_column(u'appMotoGP_pilot', 'origin_city', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Pilot.company_representative'
        db.alter_column(u'appMotoGP_pilot', 'company_representative', self.gf('django.db.models.fields.CharField')(max_length=40))

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
            'company_representative': ('django.db.models.fields.CharField', [], {'default': "'No value'", 'max_length': '200'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appMotoGP.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appMotoGP.Manufacturer']"}),
            'origin_city': ('django.db.models.fields.CharField', [], {'default': "'No value'", 'max_length': '200'}),
            'pilot_age': ('django.db.models.fields.IntegerField', [], {}),
            'pilot_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'race_win': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['appMotoGP']