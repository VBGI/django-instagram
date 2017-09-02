"""
Created on 04/sep/2016

@author: Marco Pompili

Significantly modified by Dmitry E. Kislov, 2 sept., 2017
Modifications include:
    dropping lxml, requests requirements
"""

try:
    from  urllib import urlopen
except ImportError:
    from urllib.request import urlopen

import json
import re


def instagram_scrap_profile(username):
    url = "https://www.instagram.com/{}/".format(username)
    page = urlopen(url)
    return page.read()


def instagram_profile_obj(username):
    pat = re.compile(r'\<script\s?type="text/javascript"\>\s?window\._sharedData\s?=\s?\{(.*?)\};</script>')
    data = instagram_scrap_profile(username)
    try:
        match = pat.findall(data)[-1]
    except IndexError:
        match = ''
    try:
        jsonified = json.loads(match)
    except TypeError:
        jsonified = {}
    return jsonified
