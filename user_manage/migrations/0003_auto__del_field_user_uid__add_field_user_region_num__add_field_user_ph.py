# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.uid'
        db.delete_column(u'user_manage_user', 'uid')

        # Adding field 'User.region_num'
        db.add_column(u'user_manage_user', 'region_num',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'User.phone_num'
        db.add_column(u'user_manage_user', 'phone_num',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'User.nickname'
        db.add_column(u'user_manage_user', 'nickname',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'User.uid'
        db.add_column(u'user_manage_user', 'uid',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Deleting field 'User.region_num'
        db.delete_column(u'user_manage_user', 'region_num')

        # Deleting field 'User.phone_num'
        db.delete_column(u'user_manage_user', 'phone_num')

        # Deleting field 'User.nickname'
        db.delete_column(u'user_manage_user', 'nickname')


    models = {
        u'user_manage.user': {
            'Meta': {'object_name': 'User'},
            'cid': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_num': ('django.db.models.fields.IntegerField', [], {}),
            'region_num': ('django.db.models.fields.IntegerField', [], {}),
            'ukey': ('django.db.models.fields.IntegerField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['user_manage']