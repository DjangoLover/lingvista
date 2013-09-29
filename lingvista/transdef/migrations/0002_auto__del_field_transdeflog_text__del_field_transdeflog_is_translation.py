# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'TransDefLog.text'
        db.delete_column(u'transdef_transdeflog', 'text')

        # Deleting field 'TransDefLog.is_translation'
        db.delete_column(u'transdef_transdeflog', 'is_translation')

        # Deleting field 'TransDefLog.is_definition'
        db.delete_column(u'transdef_transdeflog', 'is_definition')

        # Adding field 'TransDefLog.created_at'
        db.add_column(u'transdef_transdeflog', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'TransDefLog.translation'
        db.add_column(u'transdef_transdeflog', 'translation',
                      self.gf('django.db.models.fields.TextField')(default='', max_length='500'),
                      keep_default=False)

        # Adding field 'TransDefLog.definition'
        db.add_column(u'transdef_transdeflog', 'definition',
                      self.gf('django.db.models.fields.TextField')(default='', max_length='500'),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'TransDefLog.text'
        raise RuntimeError("Cannot reverse this migration. 'TransDefLog.text' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'TransDefLog.text'
        db.add_column(u'transdef_transdeflog', 'text',
                      self.gf('django.db.models.fields.TextField')(max_length='500'),
                      keep_default=False)

        # Adding field 'TransDefLog.is_translation'
        db.add_column(u'transdef_transdeflog', 'is_translation',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'TransDefLog.is_definition'
        db.add_column(u'transdef_transdeflog', 'is_definition',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'TransDefLog.created_at'
        db.delete_column(u'transdef_transdeflog', 'created_at')

        # Deleting field 'TransDefLog.translation'
        db.delete_column(u'transdef_transdeflog', 'translation')

        # Deleting field 'TransDefLog.definition'
        db.delete_column(u'transdef_transdeflog', 'definition')


    models = {
        u'transdef.language': {
            'Meta': {'object_name': 'Language'},
            'bingcode': ('django.db.models.fields.TextField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isocode': ('django.db.models.fields.TextField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'wikicode': ('django.db.models.fields.TextField', [], {'max_length': '10'})
        },
        u'transdef.transdeflog': {
            'Meta': {'object_name': 'TransDefLog'},
            'Source language': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'source_set'", 'to': u"orm['transdef.Language']"}),
            'Target language': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transdef_set'", 'to': u"orm['transdef.Language']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'definition': ('django.db.models.fields.TextField', [], {'max_length': "'500'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.TextField', [], {'max_length': "'200'"}),
            'translation': ('django.db.models.fields.TextField', [], {'max_length': "'500'"})
        }
    }

    complete_apps = ['transdef']