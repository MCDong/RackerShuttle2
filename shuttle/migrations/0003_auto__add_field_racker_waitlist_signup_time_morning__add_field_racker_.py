# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Racker.waitlist_signup_time_morning'
        db.add_column(u'shuttle_racker', 'waitlist_signup_time_morning',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)

        # Adding field 'Racker.waitlist_signup_time_afternoon'
        db.add_column(u'shuttle_racker', 'waitlist_signup_time_afternoon',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Racker.waitlist_signup_time_morning'
        db.delete_column(u'shuttle_racker', 'waitlist_signup_time_morning')

        # Deleting field 'Racker.waitlist_signup_time_afternoon'
        db.delete_column(u'shuttle_racker', 'waitlist_signup_time_afternoon')


    models = {
        u'shuttle.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'shuttle.racker': {
            'Meta': {'object_name': 'Racker'},
            'checked_in_afternoon': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'checked_in_afternoon'", 'null': 'True', 'to': u"orm['shuttle.Shuttle']"}),
            'checked_in_morning': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'checked_in_morning'", 'null': 'True', 'to': u"orm['shuttle.Shuttle']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'signed_in_afternoon': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'signed_in_afternoon'", 'null': 'True', 'to': u"orm['shuttle.Shuttle']"}),
            'signed_in_morning': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'signed_in_morning'", 'null': 'True', 'to': u"orm['shuttle.Shuttle']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'waiting_for_afternoon': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'waiting_for_afternoon'", 'null': 'True', 'to': u"orm['shuttle.Shuttle']"}),
            'waiting_for_morning': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'waiting_for_morning'", 'null': 'True', 'to': u"orm['shuttle.Shuttle']"}),
            'waitlist_signup_time_afternoon': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'waitlist_signup_time_morning': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'shuttle.shuttle': {
            'Meta': {'object_name': 'Shuttle'},
            'arrival_location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'arrival_location'", 'to': u"orm['shuttle.Location']"}),
            'capacity': ('django.db.models.fields.IntegerField', [], {}),
            'departure_location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'departure_location'", 'to': u"orm['shuttle.Location']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_checkedin': ('django.db.models.fields.IntegerField', [], {}),
            'num_on_waitlist': ('django.db.models.fields.IntegerField', [], {}),
            'num_signedup': ('django.db.models.fields.IntegerField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'shuttle.wifiinfo': {
            'Meta': {'object_name': 'WifiInfo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'router_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['shuttle']