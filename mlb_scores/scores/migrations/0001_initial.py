# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GamesSchedule'
        db.create_table(u'scores_gamesschedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game_date', self.gf('django.db.models.fields.DateField')()),
            ('game_id', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('espn_id', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('start_time_pdt', self.gf('django.db.models.fields.TimeField')(null=True)),
            ('start_time_local', self.gf('django.db.models.fields.TimeField')(null=True)),
            ('away', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('home', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('interleague', self.gf('django.db.models.fields.IntegerField')()),
            ('away_runs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('home_runs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('away_runs_5i', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('home_runs_5i', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('game_num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('game_status', self.gf('django.db.models.fields.CharField')(max_length=16, null=True)),
        ))
        db.send_create_signal(u'scores', ['GamesSchedule'])


    def backwards(self, orm):
        # Deleting model 'GamesSchedule'
        db.delete_table(u'scores_gamesschedule')


    models = {
        u'scores.gamesschedule': {
            'Meta': {'object_name': 'GamesSchedule'},
            'away': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'away_runs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'away_runs_5i': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'espn_id': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'game_date': ('django.db.models.fields.DateField', [], {}),
            'game_id': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'game_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'game_status': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'home': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'home_runs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'home_runs_5i': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interleague': ('django.db.models.fields.IntegerField', [], {}),
            'start_time_local': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
            'start_time_pdt': ('django.db.models.fields.TimeField', [], {'null': 'True'})
        }
    }

    complete_apps = ['scores']