# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pilot.creator'
        db.add_column(u'appMotoGP_pilot', 'creator',
                      self.gf('django.db.models.fields.CharField')(max_length=60, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Pilot.creator'
        db.delete_column(u'appMotoGP_pilot', 'creator')


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
            'creator': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'debut_circuit': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'img/no-image.png'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appMotoGP.Manufacturer']"}),
            'pilot_age': ('django.db.models.fields.IntegerField', [], {}),
            'pilot_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'race_win': ('django.db.models.fields.IntegerField', [], {}),
            'representative_company': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'})
        }
    }

    complete_apps = ['appMotoGP']