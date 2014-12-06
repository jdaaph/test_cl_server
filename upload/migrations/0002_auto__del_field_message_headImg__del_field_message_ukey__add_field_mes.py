# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Message.headImg'
        db.delete_column(u'upload_message', 'headImg')

        # Deleting field 'Message.ukey'
        db.delete_column(u'upload_message', 'ukey')

        # Adding field 'Message.message_key'
        db.add_column(u'upload_message', 'message_key',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=30),
                      keep_default=False)

        # Adding field 'Message.send_time'
        db.add_column(u'upload_message', 'send_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 12, 6, 0, 0)),
                      keep_default=False)

        # Adding field 'Message.img'
        db.add_column(u'upload_message', 'img',
                      self.gf('django.db.models.fields.files.FileField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Message.headImg'
        db.add_column(u'upload_message', 'headImg',
                      self.gf('django.db.models.fields.files.FileField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Message.ukey'
        db.add_column(u'upload_message', 'ukey',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=30),
                      keep_default=False)

        # Deleting field 'Message.message_key'
        db.delete_column(u'upload_message', 'message_key')

        # Deleting field 'Message.send_time'
        db.delete_column(u'upload_message', 'send_time')

        # Deleting field 'Message.img'
        db.delete_column(u'upload_message', 'img')


    models = {
        u'upload.message': {
            'Meta': {'ordering': "('receiver_uid',)", 'object_name': 'Message'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'message_key': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'receiver_uid': ('django.db.models.fields.IntegerField', [], {}),
            'send_time': ('django.db.models.fields.DateTimeField', [], {}),
            'sender_uid': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['upload']