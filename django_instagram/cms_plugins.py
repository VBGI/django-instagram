# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from .models import Instagram
from django.utils.translation import ugettext_lazy as _


class InstagramPlugin(CMSPluginBase):
    model = Instagram
    name = _(u"Изображения Instagram")
    render_template = "django_instagram/instagram.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance})
        return context