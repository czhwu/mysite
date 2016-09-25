# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from taggit.managers import TaggableManager


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return ('dpress_category', None, {
            'category': self.slug
        })
    get_absolut_url = models.permalink(get_absolut_url)


class Post(models.Model):
    STATUS_CHOICES = (
        (1, u'草稿'),
        (2, u'已发布'),
    )
    title = models.CharField(u'标题', max_length=200)
    author = models.ForeignKey(User, related_name='added_posts')
    body = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    pub_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=datetime.now)
    update_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', related_name='posts', blank=True, null=True, default=None, on_delete=models.SET_NULL)
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'

    def __str__(self):
        return self.title

    def publish(self):
        self.pub_date = datetime.now()
        self.save()


