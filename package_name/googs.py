#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

GOOGLE_ADDRESS = "https://www.google.com"


def can_get_to_google():
    try:
        req = requests.get(GOOGLE_ADDRESS)
        req.raise_for_status()
    except requests.HTTPError:
        return False
    else:
        return True
