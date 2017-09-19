# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page, never_cache
from .models import Instagram
from .scraper import instagram_profile_obj
import re
import json

mlength = Instagram._meta.get_field('username').max_length

@csrf_exempt
@never_cache
def get_instagram_data(request, username):
    print(username)
    if re.match(r'[a-zA-Z_]+', username) and len(username) < mlength:
        profile = instagram_profile_obj(username=username)
        media = profile['entry_data']['ProfilePage'][-1]['user']['media']['nodes']
        return HttpResponse(json.dumps(media), content_type="application/json")
    else:
        return HttpResponse('[]', content_type="application/json")