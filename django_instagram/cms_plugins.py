# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from .models import Instagram
from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from django.conf import settings

class InstagramPlugin(CMSPluginBase):
    model = Instagram
    name = _(u"Изображения Instagram")
    render_template = "django_instagram/instagram.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance})
        return context

    def icon_src(self, instance):
        return getattr(settings, 'STATIC_URL', '') + "/django_instagram/images/" + "instagram-icon.png"

plugin_pool.register_plugin(InstagramPlugin)