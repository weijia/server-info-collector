# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NetworkElement'
        db.create_table('server_info_collector_networkelement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('port', self.gf('django.db.models.fields.IntegerField')(default=22)),
            ('os', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='parent_network_element', null=True, to=orm['server_info_collector.NetworkElement'])),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('memory_size_in_m', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('model_or_part_number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cpu_info', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('hard_disk_size_in_m', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('other_info', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('server_info_collector', ['NetworkElement'])


    def backwards(self, orm):
        # Deleting model 'NetworkElement'
        db.delete_table('server_info_collector_networkelement')


    models = {
        'server_info_collector.networkelement': {
            'Meta': {'object_name': 'NetworkElement'},
            'cpu_info': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'hard_disk_size_in_m': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'memory_size_in_m': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'model_or_part_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'os': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'other_info': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'parent_network_element'", 'null': 'True', 'to': "orm['server_info_collector.NetworkElement']"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': '22'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['server_info_collector']