"""
Created on 12/dic/2013

@author: Marco Pompili

Significantly modified by Dmitry E. Kislov, 2 sept., 2017
"""

from django import template
from django_instagram.scraper import instagram_profile_obj

register = template.Library()

def get_profile_media(profile, page = 0):
    """
    Parse a generated media object
    :param profile:
    :param page:
    :return:
    """
    return profile['entry_data']['ProfilePage'][page]['user']['media']['nodes']


class InstagramUserRecentMediaNode(template.Node):
    """
    Template node for showing recent media from an user.
    """

    def __init__(self, username):
        self.username = username

    def render(self, context):
        profile = instagram_profile_obj(username=self.username)
        context['profile'] = profile
        context['recent_media'] = get_profile_media(profile)

        return ''


@register.tag
def instagram_user_recent_media(parser, token):
    """
    Tag for getting data about recent media of an user.
    :param parser:
    :param token:
    :return:
    """
    try:
        tagname, username = token.split_contents()

        return InstagramUserRecentMediaNode(username)
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument" % token.contents.split()[0]
        )


@register.inclusion_tag('django_instagram/recent_media_box.html')
def instagram_recent_media_box(*args, **kwargs):
    profile = instagram_profile_obj(username=kwargs.get('username'))
    recent_media = get_profile_media(profile)

    return {
        'profile': profile,
        'recent_media': recent_media
    }