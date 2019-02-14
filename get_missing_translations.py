#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from locales import Locales

print("content-type:text/html\n\n")

locales_obj = Locales('en')
print(locales_obj.get_missing_translations())
