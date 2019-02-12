#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

print("content-type:text/html\n\n")

import cgi
import cgitb
#cgitb.enable()  # for troubleshooting
from jinja2 import Template, Environment, PackageLoader

from locales import Locales

locales_obj = Locales('en')
locales = locales_obj.get_locales()

env  = Environment(loader=PackageLoader('achtelbass', 'templates'))
template = env.get_template('imprint.html')
context  = {}

context['locales'] = locales

form = cgi.FieldStorage()

def index():

    print(template.render(context))

index()
