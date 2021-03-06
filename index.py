#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

print("content-type:text/html\n\n")

import cgi
import cgitb
#cgitb.enable()  # for troubleshooting

import os

from jinja2 import Template, Environment, PackageLoader

from achtelbass import achtelbass

from locales import Locales

env  = Environment(loader=PackageLoader('achtelbass', 'templates'))
template = env.get_template('index.html')
context  = {}

form = cgi.FieldStorage()

def index():

	parameters = {'tonic'				   : form.getvalue('tonic', 'C'),
				  'mode'					: form.getvalue('mode', 'Major'),
				  'grand_staff'			 : form.getvalue('grand_staff', False),
				  'chords_frequency'		: form.getvalue('chords_frequency', 0),
				  'intervals'			   : form.getlist('intervals') or ['Second'],
				  'inversion'			   : False,
				  'min_pitch'			   : form.getvalue('min_pitch', 'C'),
				  'max_pitch'			   : form.getvalue('max_pitch', 'c'),
				  'rest_frequency'		  : form.getvalue('rest_frequency', 0),
				  'time_signature'		  : form.getvalue('time_signature','4/4'),
				  'note_values'			 : form.getlist('note_values') or ['1', '1/2', '1/4'],
				  'tuplets'				 : form.getlist('tuplets') or [3],
				  'tuplet_same_pitch'	   : False,
				  'tuplets_frequency'	   : form.getvalue('tuplets_frequency',0),
				  'prolongations'		   : False,
				  'prolongations_frequency' : 0,
				  'bpm'					 : 60,
				  'tempo'				   : 'andante',
				  'amount_of_bars'		   : form.getvalue('amount_of_bars', 8),
				 }

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
	locales = locales_obj.get_locales()

	# Locales checks for valid languages defaulting to en
	parameters['language'] = locales_obj.Language_Code
	language = locales_obj.Language_Code
	
	# Sanitize form input, discard everything containing "<"
	# as it starts html and javascript tags indicating xss
	for dict_key in parameters:
		if isinstance(parameters.get(dict_key, 'foo'), str):
			if '<' in parameters.get(dict_key, 'foo'):
				parameters[dict_key] = 'character "lower than" detected for parameter' + dict_key + '. Suspecting cross site scripting attempt.'

	achtelbass_obj = achtelbass.Achtelbass(parameters, locales)
	
	context.update(achtelbass_obj.__dict__)
	
	context['locales'] = locales
	
	context['preselected'] = parameters
	
	context['language'] = language

	context['note_value_symbols'] = {
		'1'	: '𝅝',
		'1/2'  : '𝅗𝅥',
		'1/4'  : '♩',
		'1/8'  : '♪',
		'1/16' : '𝅘𝅥𝅯',
		'1/32' : '𝅘𝅥𝅰',
		'1/64' : '𝅘𝅥𝅱',
	}

	context['note_value_names'] =  achtelbass_obj.Note_Names
	
	context['generated_notes'] = achtelbass_obj.display()
	
	# If cookie for hiding controls is set and form was submitted
	# Tonic is always set when the form is submitted
	if form.getvalue('tonic') and 'hide_controls_after_submit' in parameters:
		# The form was submitted.
		# Show result notes, but hide the controls.
		context['controls_display_style'] = 'none'
		context['controls_button_text'] = locales['show_controls']
	else:
		# Show controls and notes.
		context['controls_display_style'] = 'block'
		context['controls_button_text'] = locales['hide_controls']
	

	print(template.render(context))

index()
