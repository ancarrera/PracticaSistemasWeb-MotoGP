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
            ('origin_city', self.gf('django.db.models.fields.CharField')(default='No value', max_length=40)),
            ('company_representative', self.gf('django.db.models.fields.CharField')(default='No value', max_length=40)),
            ('manufacturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appMotoGP.Manufacturer'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appMotoGP.Country'])),
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
            'company_representative': ('django.db.models.fields.CharField', [], {'default': "'No value'", 'max_length': '40'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appMotoGP.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appMotoGP.Manufacturer']"}),
            'origin_city': ('django.db.models.fields.CharField', [], {'default': "'No value'", 'max_length': '40'}),
            'pilot_age': ('django.db.models.fields.IntegerField', [], {}),
            'pilot_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'race_win': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['appMotoGP']