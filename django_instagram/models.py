# -*- coding: utf-8 -*-

from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Instagram(CMSPlugin):
    username = models.CharField(max_length=30, default='', verbose_name=_('Instagram username'))
    delay = models.IntegerField(verbose_name=_(u'задержка, мс'), default=3000)
    num = models.IntegerField(verbose_name=_(u'макисмальное число фотографий'), default=5)
    size = models.IntegerField(verbose_name=_(u'размер изображения'), default=150)

    def __unicode__(self):
        return '|'.join([self.username, str(self.delay), str(self.num), str(self.size)])
