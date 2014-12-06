# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'user_manage_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.IntegerField')()),
            ('cid', self.gf('django.db.models.fields.IntegerField')()),
            ('ukey', self.gf('django.db.models.fields.IntegerField')(max_length=30)),
        ))
        db.send_create_signal(u'user_manage', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'user_manage_user')


    models = {
        u'user_manage.user': {
            'Meta': {'object_name': 'User'},
            'cid': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uid': ('django.db.models.fields.IntegerField', [], {}),
            'ukey': ('django.db.models.fields.IntegerField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['user_manage']