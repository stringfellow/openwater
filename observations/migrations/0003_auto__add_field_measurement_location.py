# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Measurement.location'
        sql = """
        SELECT AddGeometryColumn('observations_measurement', 'location', 4326, 'POINT', 2);
        ALTER TABLE "observations_measurement" ALTER "location" SET NOT NULL;
        CREATE INDEX "observations_measurement_location_id" ON "observations_measurement" USING GIST ( "location" );
        """
        db.execute(sql)

    def backwards(self, orm):
        # Deleting field 'Measurement.location'
        db.delete_column(u'observations_measurement', 'location')


    models = {
        u'observations.measurement': {
            'Meta': {'object_name': 'Measurement'},
            'created_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'observations': ('django_hstore.fields.DictionaryField', [], {'db_index': 'True'}),
            'observer': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'reference_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['observations']
