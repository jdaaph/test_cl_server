# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.reg_time'
        db.add_column(u'user_manage_user', 'reg_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)


        # Changing field 'User.phone_num'
        db.alter_column(u'user_manage_user', 'phone_num', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'User.ukey'
        db.alter_column(u'user_manage_user', 'ukey', self.gf('django.db.models.fields.CharField')(max_length=30))

    def backwards(self, orm):
        # Deleting field 'User.reg_time'
        db.delete_column(u'user_manage_user', 'reg_time')


        # Changing field 'User.phone_num'
        db.alter_column(u'user_manage_user', 'phone_num', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'User.ukey'
        db.alter_column(u'user_manage_user', 'ukey', self.gf('django.db.models.fields.IntegerField')(max_length=30))

    models = {
        u'user_manage.user': {
            'Meta': {'object_name': 'User'},
            'cid': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_num': ('django.db.models.fields.BigIntegerField', [], {}),
            'reg_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'region_num': ('django.db.models.fields.IntegerField', [], {}),
            'ukey': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['user_manage']