# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Language'
        db.create_table(u'transdef_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isocode', self.gf('django.db.models.fields.TextField')(max_length=10)),
            ('bingcode', self.gf('django.db.models.fields.TextField')(max_length=10)),
            ('wikicode', self.gf('django.db.models.fields.TextField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'transdef', ['Language'])

        # Adding model 'TransDefLog'
        db.create_table(u'transdef_transdeflog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(related_name='log', to=orm['account.Account'])),
            ('source', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('translation', self.gf('django.db.models.fields.TextField')(max_length=200, null=True)),
            ('definition', self.gf('django.db.models.fields.TextField')(max_length=200, null=True)),
            ('lang_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='source_set', to=orm['transdef.Language'])),
            ('lang_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='transdef_set', to=orm['transdef.Language'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'transdef', ['TransDefLog'])


    def backwards(self, orm):
        # Deleting model 'Language'
        db.delete_table(u'transdef_language')

        # Deleting model 'TransDefLog'
        db.delete_table(u'transdef_transdeflog')


    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['transdef.Language']"}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'transdef.language': {
            'Meta': {'ordering': "['name']", 'object_name': 'Language'},
            'bingcode': ('django.db.models.fields.TextField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isocode': ('django.db.models.fields.TextField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'wikicode': ('django.db.models.fields.TextField', [], {'max_length': '10'})
        },
        u'transdef.transdeflog': {
            'Meta': {'object_name': 'TransDefLog'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'log'", 'to': u"orm['account.Account']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'definition': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'source_set'", 'to': u"orm['transdef.Language']"}),
            'lang_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transdef_set'", 'to': u"orm['transdef.Language']"}),
            'source': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'translation': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['transdef']