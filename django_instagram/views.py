# -*- coding: utf-8 -*-

from django.http import HttpResponse
from .models import Instagram
from .scraper import instagram_profile_obj
import re


mlength = Instagram._meta.get_field('name').max_length

def get_instagram_data(request, username):

    if re.match(r'[a-zA-Z_]+', username) and len(username) < mlength:
        profile = instagram_profile_obj(username=username)
        media = profile['entry_data']['ProfilePage']['page']['user']['media']['nodes']
        return HttpResponse(media, content_type="application/json")
    else:
        return HttpResponse('[]', content_type="application/json")