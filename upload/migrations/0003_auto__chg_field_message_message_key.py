# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Message.message_key'
        db.alter_column(u'upload_message', 'message_key', self.gf('django.db.models.fields.CharField')(max_length=32))

    def backwards(self, orm):

        # Changing field 'Message.message_key'
        db.alter_column(u'upload_message', 'message_key', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        u'upload.message': {
            'Meta': {'ordering': "('receiver_uid',)", 'object_name': 'Message'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'message_key': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'receiver_uid': ('django.db.models.fields.IntegerField', [], {}),
            'send_time': ('django.db.models.fields.DateTimeField', [], {}),
            'sender_uid': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['upload']