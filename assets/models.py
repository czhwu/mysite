from django.db import models
from datetime import datetime
import django.utils.timezone as timezone


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, default='苏州中兴联')

    def __str__(self):
        return self.name


class AssetDetail(models.Model):
    STATE_CHOICES = (
        ('SY', '使用'),
        ('JC', '借出'),
        ('ZC', '暂存'),
    )
    gdzc = models.CharField('资产编号', max_length=20)
    name = models.CharField('分类', max_length=30)
    discription = models.CharField('描述', max_length=300)
    add_date = models.DateTimeField('入账日期', default=timezone.now)
    mod_date = models.DateTimeField('最后更新日期', blank=True, null=True, auto_now=True)
    scrap_date = models.DateTimeField('报废日期', blank=True, null=True,  default=timezone.now)
    dpt = models.ForeignKey(Department, blank=True, null=True)                                # todo:添加部门
    user = models.CharField('保管员', max_length=200)
    ip = models.GenericIPAddressField('IP地址', blank=True, null=True)
    state = models.CharField('状态', max_length=2, choices=STATE_CHOICES, default='SY')

    class Meta:
        ordering = ['dpt', 'gdzc']

    def __str__(self):
        return self.gdzc

    def scrap(self):
        self.scrap_date = timezone.now()
        self.save()

class Lend(models.Model):
    gdzc = models.ForeignKey(AssetDetail)
    dpt = models.ForeignKey(Department)
    reason = models.CharField(max_length=300)
    lend_time = models.DateTimeField('借出时间', auto_now=True)
    back_time = models.DateTimeField('归还时间', blank=True, null=True)
    user = models.CharField('借用人', max_length=200)

    def __str__(self):
        return self.gdzc

    def back(self):
        self.back_time = timezone.now()
        self.save()
