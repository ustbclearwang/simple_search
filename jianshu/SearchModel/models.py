
from __future__ import unicode_literals

from django.db import models


class SearchData(models.Model):
    id = models.IntegerField(primary_key=True)
    search_keyword = models.CharField(max_length=255, blank=True, null=True)
    task_data_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_data'


class TaskData(models.Model):
    id = models.IntegerField(primary_key=True)
    time = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    article_title = models.CharField(max_length=255, blank=True, null=True)
    article_content = models.CharField(max_length=255, blank=True, null=True)
    article_publish_time = models.CharField(max_length=255, blank=True, null=True)
    article_thumbnail = models.CharField(max_length=255, blank=True, null=True)
    article_author = models.CharField(max_length=255, blank=True, null=True)
    article_avatar = models.CharField(max_length=255, blank=True, null=True)
    article_topics = models.CharField(max_length=255, blank=True, null=True)
    views_count = models.CharField(max_length=255, blank=True, null=True)
    comments_count = models.CharField(max_length=255, blank=True, null=True)
    clikes_count = models.CharField(max_length=255, blank=True, null=True)
    words_count = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_data'
