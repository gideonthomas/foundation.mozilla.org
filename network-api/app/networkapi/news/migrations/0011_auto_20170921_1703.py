# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-21 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import networkapi.news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_remove_news_homepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='glyph',
            field=models.FileField(blank=True, help_text='Image associated with the article source. Unsure of what to use? Leave blank and ask a designer', max_length=2048, null=True, upload_to=networkapi.news.models.get_news_glyph_upload_path),
        ),
    ]
