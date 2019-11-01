"""
Created on 04/sep/2016

@author: Marco Pompili

Significantly modified by Dmitry E. Kislov, 2 sept., 2017
"""

try:
    from  urllib import urlopen
except ImportError:
    from urllib.request import urlopen

import json
import re

_pat = re.compile(b'\<script\s?type="text/javascript"\>\s?window\._sharedData\s?=\s?\{(.*?)\};</script>')


def instagram_scrap_profile(username):
    url = "https://www.instagram.com/{}/".format(username)
    data = urlopen("https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json").read()
    proxies = json.loads(data)
    for proxy in proxies['proxies']:
        if proxy['google_status'] == 200:
            candidate = {'http': "http://{}:{}/".format(proxy['ip'], proxy['port'])}
            page = urlopen(url, proxies=candidate)
            if page.getcode() == 200:
                return page.read()
    else:
        return ''


def instagram_profile_obj(username):
    data = instagram_scrap_profile(username)
    try:
        match = _pat.findall(data)[-1]
    except IndexError:
        match = ''
    try:
        jsonified = json.loads("{" + match.decode('utf-8') + "}")
    except (TypeError, ValueError):
        jsonified = {}
    return jsonified
