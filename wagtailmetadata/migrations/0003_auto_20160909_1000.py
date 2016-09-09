# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 00:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmetadata', '0002_auto_20160607_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitemetadatapreferences',
            name='site_image',
            field=models.ForeignKey(blank=True, help_text='\n        This is the default image that will be shown when your page is\n         shared on social media or is found on search engines ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
