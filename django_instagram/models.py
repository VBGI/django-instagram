from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _


class Instagram(CMSPlugin):
    delay = models.IntegerField(verbose_name=_(u'Задержка, мс'), default=3000)
    num = models.IntegerField(verbose_name=_