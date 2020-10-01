#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

print("content-type:text/html\n\n")

import cgi
import cgitb
#cgitb.enable()  # for troubleshooting
import os
from jinja2 import Template, Environment, PackageLoader

from locales import Locales

env  = Environment(loader=PackageLoader('achtelbass', 'templates'))
template = env.get_template('configuration.html')
context  = {}


form = cgi.FieldStorage()

def index():
	
	parameters = {}
	
	# language defaults to english
	# but is overridden by cookie
	# which is overridden by GET parameter
	parameters['language'] = 'en'

	# Cookies override cgi forms
	if 'HTTP_COOKIE' in os.environ:
		cookies_string = os.environ['HTTP_COOKIE']
		cookies_list = cookies_string.split('; ')

		for cookie in cookies_list:
			cookie = cookie.split('=')
			parameters[cookie[0]] = cookie[1]
			
			# some form fields are supposed to yield an array
			if cookie[0] in ['intervals', 'note_values', 'tuplets']:
				parameters[cookie[0]] = [cookie[1]]
				
				# if more than one value was selected: ### is the custom
				# record separator in the cookie
				values_list = cookie[1].split('###')
				if len(values_list) > 1:
					parameters[cookie[0]] = values_list
	
	# GET parameter overrides cookie, important for sitemap
	language = form.getvalue('language', parameters['language'])

	locales_obj = Locales(language)
	
	# Locales checks for valid languages defaulting to en
	parameters['language'] = locales_obj.Language_Code
	language = locales_obj.Language_Code
	
	# Sanitize form input, discard everything containing "<"
	# as it starts html and javascript tags indicating xss
	for dict_key in parameters:
		if isinstance(parameters.get(dict_key, 'foo'), str):
			if '<' in parameters.get(dict_key, 'foo'):
				parameters[dict_key] = 'character "lower than" detected for parameter' + dict_key + '. Suspecting cross site scripting attempt.'

	context['locales'] = locales_obj.get_locales()
	context['language'] = language

	print(template.render(context))

index()
