#!/usr/bin/python2.6
# -*- coding: utf-8 -*- 

print "content-type:text/html\n\n"

import cgi
import cgitb
#cgitb.enable()  # for troubleshooting
from jinja2 import Template, Environment, PackageLoader

env  = Environment(loader=PackageLoader('achtelbass', 'templates'))
template = env.get_template('about.html')
context  = {}

form = cgi.FieldStorage()

def index():

    print template.render(context)

index()
