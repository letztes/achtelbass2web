#!/usr/bin/python
# -*- coding: utf-8 -*- 

print "content-type:text/html\n\n"

import cgi
import cgitb
#cgitb.enable()  # for troubleshooting
from jinja2 import Template, Environment, PackageLoader

from achtelbass import achtelbass

from locales_en import locales

env  = Environment(loader=PackageLoader('achtelbass', 'templates'))
template = env.get_template('index.html')
context  = {}

form = cgi.FieldStorage()

def index():

    parameters = {'tonic'                   : form.getvalue('tonic', 'C'),
                  'mode'                    : form.getvalue('mode', 'Major'),
                  'grand_staff'             : form.getvalue('grand_staff', False),
                  'chords_frequency'        : form.getvalue('chords_frequency', 0),
                  'intervals'               : form.getlist('intervals') or ['Second'],
                  'inversion'               : False,
                  'min_pitch'               : form.getvalue('min_pitch', 'C'),
                  'max_pitch'               : form.getvalue('max_pitch', 'c'),
                  'rest_frequency'          : form.getvalue('rest_frequency', 0),
                  'time_signature'          : form.getvalue('time_signature','4/4'),
                  'note_values'             : form.getlist('note_values') or ['1', '1/2', '1/4'],
                  'tuplets'                 : form.getlist('tuplets') or [0],
                  'tuplet_same_pitch'       : False,
                  'tuplets_frequency'       : form.getvalue('tuplets_frequency',0),
                  'prolongations'           : False,
                  'prolongations_frequency' : 0,
                  'bpm'                     : 60,
                  'tempo'                   : 'andante',
                 }
    
    
    achtelbass_obj = achtelbass.Achtelbass(parameters, locales)
    
    context.update(achtelbass_obj.__dict__)
    
    context['preselected'] = parameters

    context['note_value_symbols'] = {
        '1'    : u'𝅝',
        '1/2'  : u'𝅗𝅥',
        '1/4'  : u'♩',
        '1/8'  : u'♪',
        '1/16' : u'𝅘𝅥𝅯',
        '1/32' : u'𝅘𝅥𝅰',
        '1/64' : u'𝅘𝅥𝅱',
    }

    context['note_value_names'] =  achtelbass_obj.Note_Names
    
    context['generated_notes'] = achtelbass_obj.display()

    print template.render(context)

index()
