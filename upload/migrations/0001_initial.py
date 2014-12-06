# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table(u'upload_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender_uid', self.gf('django.db.models.fields.IntegerField')()),
            ('receiver_uid', self.gf('django.db.models.fields.IntegerField')()),
            ('ukey', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('headImg', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'upload', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table(u'upload_message')


    models = {
        u'upload.message': {
            'Meta': {'ordering': "('receiver_uid',)", 'object_name': 'Message'},
            'headImg': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receiver_uid': ('django.db.models.fields.IntegerField', [], {}),
            'sender_uid': ('django.db.models.fields.IntegerField', [], {}),
            'ukey': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['upload']