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
            ('source', self.gf('django.db.models.fields.TextField')(max_length='200')),
            ('text', self.gf('django.db.models.fields.TextField')(max_length='500')),
            ('is_definition', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_translation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Source language', self.gf('django.db.models.fields.related.ForeignKey')(related_name='source_set', to=orm['transdef.Language'])),
            ('Target language', self.gf('django.db.models.fields.related.ForeignKey')(related_name='transdef_set', to=orm['transdef.Language'])),
        ))
        db.send_create_signal(u'transdef', ['TransDefLog'])


    def backwards(self, orm):
        # Deleting model 'Language'
        db.delete_table(u'transdef_language')

        # Deleting model 'TransDefLog'
        db.delete_table(u'transdef_transdeflog')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_definition': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_translation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.TextField', [], {'max_length': "'200'"}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': "'500'"})
        }
    }

    complete_apps = ['transdef']