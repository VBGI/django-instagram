# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from .models import Instagram
from .scraper import instagram_profile_obj
import re
import json

mlength = Instagram._meta.get_field('username').max_length

@csrf_exempt
@cache_page(40000)
def get_instagram_data(request, username):
    if re.match(r'[a-zA-Z_]+', username) and len(username) < mlength:
        profile = instagram_profile_obj(username=username)
        try:
            media = profile['entry_data']['ProfilePage'][-1]['user']['media']['nodes']
        except KeyError:
            try:
                media = profile['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
            except KeyError:
                media = dict()
        result = []
        for k in range(len(media)):
            result.append(dict())
            try:
                result[k].update({'caption': media[k]['caption'].replace('#', ' #')})
            except:
                result[k].update({'caption': media[k]['node']['edge_media_to_caption']['edges'][-1]['node']['text'].replace('#', ' #')})
                result[k].update({'thumbnail_src': media[k]['node']['thumbnail_src']})
        return HttpResponse(json.dumps(result), content_type="application/json")
    else:
        return HttpResponse('[]', content_type="application/json")
