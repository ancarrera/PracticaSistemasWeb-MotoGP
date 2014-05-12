# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'appMotoGP_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal(u'appMotoGP', ['Country'])

        # Adding model 'Manufacturer'
        db.create_table(u'appMotoGP_manufacturer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('manufacturer_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appMotoGP.Country'])),
        ))
        db.send_create_signal(u'appMotoGP', ['Manufacturer'])

        # Adding model 'Pilot'
        db.create_table(u'appMotoGP_pilot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pilot_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('pilot_age', self.gf('django.db.models.fields.IntegerField')()),
            ('race_win', self.gf('django.db.models.fields.IntegerField')()),
            ('representative_company', self.gf('django.db.models.fields.CharField')(max_length=60, null=True)),
            ('debut_circuit', self.gf('django.db.models.fields.CharField')(max_length=60, null=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('manufacturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appMotoGP.Manufacturer'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appMotoGP.Country'])),
            ('race_winwww', self.gf('django.db.models.fields.IntegerField')(default='sfgs')),
        ))
        db.send_create_signal(u'appMotoGP', ['Pilot'])

        # Adding model 'Category'
        db.create_table(u'appMotoGP_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal(u'appMotoGP', ['Category'])

        # Adding M2M table for field manufacturer on 'Category'
        m2m_table_name = db.shorten_name(u'appMotoGP_category_manufacturer')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm[u'appMotoGP.category'], null=False)),
            ('manufacturer', models.ForeignKey(orm[u'appMotoGP.manufacturer'], null=False))
        ))
        db.create_unique(m2m_table_name, ['category_id', 'manufacturer_id'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'appMotoGP_country')

        # Deleting model 'Manufacturer'
        db.delete_table(u'appMotoGP_manufacturer')

        # Deleting model 'Pilot'
        db.delete_table(u'appMotoGP_pilot')

        # Deleting model 'Category'
        db.delete_table(u'appMotoGP_category')

        # Removing M2M table for field manufacturer on 'Category'
        db.delete_table(db.shorten_name(u'appMotoGP_category_manufacturer'))


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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appMotoGP.Manufacturer']"}),
            'pilot_age': ('django.db.models.fields.IntegerField', [], {}),
            'pilot_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'race_win': ('django.db.models.fields.IntegerField', [], {}),
            'race_winwww': ('django.db.models.fields.IntegerField', [], {'default': "'sfgs'"}),
            'representative_company': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'})
        }
    }

    complete_apps = ['appMotoGP']