#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Locales(object):
	def __init__(self, language_code):
		
		self.Language_Code = language_code
		
		self.Translations = {
# Menu
			'Home' : {
				'en' : 'Home',
			},
			'Configuration' : {
				'en' : 'Configuration',
			},
			'Imprint' : {
				'en' : 'Imprint',
			},
			'About' : {
				'en' : 'About',
			},
# Tonic
			'Tonic' : {
				'en' : 'Tonic',
			},
			'C' : {
				'en' : 'C',
			},
			'G' : {
				'en' : 'G',
			},
			'D' : {
				'en' : 'D',
			},
			'A' : {
				'en' : 'A',
			},
			'E' : {
				'en' : 'E',
			},
			'B' : {
				'en' : 'B',
			},
			'F#' : {
				'en' : 'F#',
			},
			'C#' : {
				'en' : 'C#',
			},
			'G#' : {
				'en' : 'G#',
			},
			'D#' : {
				'en' : 'D#',
			},
			'A#' : {
				'en' : 'A#',
			},
			'Gb' : {
				'en' : 'Gb',
			},
			'Db' : {
				'en' : 'Db',
			},
			'Ab' : {
				'en' : 'Ab',
			},
			'Eb' : {
				'en' : 'Eb',
			},
			'Bb' : {
				'en' : 'Bb',
			},
			'F' : {
				'en' : 'F',
			},
# min pitch and max pitch
			'c1' : {
				'en' : 'c1',
			},
			'd1' : {
				'en' : 'd1',
			},
			'e1' : {
				'en' : 'e1',
			},
			'f1' : {
				'en' : 'f1',
			},
			'g1' : {
				'en' : 'g1',
			},
			'a1' : {
				'en' : 'a1',
			},
			'b1' : {
				'en' : 'b1',
			},
			'c2' : {
				'en' : 'c2',
			},
			'd2' : {
				'en' : 'd2',
			},
			'e2' : {
				'en' : 'e2',
			},
			'f2' : {
				'en' : 'f2',
			},
			'g2' : {
				'en' : 'g2',
			},
			'a2' : {
				'en' : 'a2',
			},
			'b2' : {
				'en' : 'b2',
			},
			'c3' : {
				'en' : 'c3',
			},
			'd3' : {
				'en' : 'd3',
			},
			'e3' : {
				'en' : 'e3',
			},
			'f3' : {
				'en' : 'f3',
			},
			'g3' : {
				'en' : 'g3',
			},
			'a3' : {
				'en' : 'a3',
			},
			'b3' : {
				'en' : 'b3',
			},
			'c4' : {
				'en' : 'c4',
			},
			'd4' : {
				'en' : 'd4',
			},
			'e4' : {
				'en' : 'e4',
			},
			'f4' : {
				'en' : 'f4',
			},
			'g4' : {
				'en' : 'g4',
			},
			'a4' : {
				'en' : 'a4',
			},
			'b4' : {
				'en' : 'b4',
			},
			'c5' : {
				'en' : 'c5',
			},
			'd5' : {
				'en' : 'd5',
			},
			'e5' : {
				'en' : 'e5',
			},
			'f5' : {
				'en' : 'f5',
			},
			'g5' : {
				'en' : 'g5',
			},
			'a5' : {
				'en' : 'a5',
			},
			'b5' : {
				'en' : 'b5',
			},
# Mode
			'Mode' : {
				'en' : 'Mode',
			},
			'Major' : {
				'en' : 'Major',
			},
			'Minor' : {
				'en' : 'Minor',
			},
			'Changing key' : {
				'en' : 'Changing key',
			},
# Interval
			'Interval' : {
				'en' : 'Interval',
			},
			'Intervals' : {
				'en' : 'Intervals',
			},
			'Unison' : {
				'en' : 'Unison',
			},
			'Second' : {
				'en' : 'Second',
			},
			'Third' : {
				'en' : 'Third',
			},
			'Fourth' : {
				'en' : 'Fourth',
			},
			'Fifth' : {
				'en' : 'Fifth',
			},
			'Sixth' : {
				'en' : 'Sixth',
			},
			'Seventh' : {
				'en' : 'Seventh',
			},
			'Octave' : {
				'en' : 'Octave',
			},
			'Inversion' : {
				'en' : 'Inversion',
			},
# Rest
			'Rests' : {
				'en' : 'Rests',
			},
# Time signature
			'time_signature' : {
				'en' : 'Time signature',
			},
# Note value
			'note_values' : {
				'en' : 'Note values',
			},
# Tempo
			'Tempo' : {
				'en' : 'Tempo',
			},
# Tuplet
			'Triplets' : {
				'en' : 'Triplets',
			},
			'Tuplets' : {
				'en' : 'Tuplets',
			},
			'None' : {
				'en' : 'None',
			},
			'2' : {
				'en' : '2',
			},
			'3' : {
				'en' : '3',
			},
			'4' : {
				'en' : '4',
			},
			'5' : {
				'en' : '5',
			},
			'6' : {
				'en' : '6',
			},
			'7' : {
				'en' : '7',
			},
			'Tuplet frequency' : {
				'en' : 'Tuplet frequency',
			},
# Chords
			'Chords' : {
				'en' : 'Chords',
			},
# Frequency values
			'0.1' : {
				'en' : '10 %',
			},
			'0.2' : {
				'en' : '20 %',
			},
			'0.3' : {
				'en' : '30 %',
			},
			'0.4' : {
				'en' : '40 %',
			},
			'0.5' : {
				'en' : '50 %',
			},
			'0.6' : {
				'en' : '60 %',
			},
			'0.7' : {
				'en' : '70 %',
			},
			'0.8' : {
				'en' : '80 %',
			},
			'0.9' : {
				'en' : '90 %',
			},
			'1' : {
				'en' : '100 %',
			},
# Configuration of website
			'enable_cookies' : {
				'en' : 'Enable cookies for saving configuration for next visit of this website',
			},
			'hide_controls_after_submit' : {
				'en' : 'Hide controls after each submit',
			},
			'set_amount_of_bars' : {
				'en' : 'Set amount of bars',
			},
# About page
			'achtelbass_is_helpful' : {
				'en' : 'Achtelbass is meant to help you practice sight reading at your individual level.',
			},
			'contains_random_generator' : {
				'en' : 'All notes are randomly generated and very unlikely to be seen ever again in the same combination.',
			},
			'no_memorization_effect' : {
				'en' : 'This way you will not memorize the notes of the exercise as it happens often with traditional literature.',
			},
			'achtelbass_is_versatile' : {
				'en' : 'You can increase the difficulty level gradually by adding options evenly or concentrate on certain options like triplets, chords, exotic time signatures or whatever you want to master.',
			},
			'achtelbass_is_versatile_really' : {
				'en' : 'Prepare for exams, target your personal weak spots or just begin to learn sight reading.',
			},
			'free_2_play' : {
				'en' : 'Achtelbass is free of charge and does not bother you with advertisement.',
			},
			'please_contact_me' : {
				'en' : 'If you miss a feature or find a bug please contact me at',
			},
			'please_report_issues' : {
				'en' : 'or open an issue at',
			},
			'please_fork_the_repo' : {
				'en' : 'If you are into python then you might fork the project and fix the issue by yourself.',
			},
			'request_for_donation' : {
				'en' : 'If you do not code but like the website and want to contribute you can make a donation.',
			},
# General stuff
			'hide_controls' : {
				'en' : 'Hide controls',
			},
			'show_controls' : {
				'en' : 'Show controls',
			},
			'generate_new' : {
				'en' : 'Generate new',
			},
			'download_midi' : {
				'en' : 'Download midi',
			},
			'Warning' : {
				'en' : 'Warning',
			},
			'OK' : {
				'en' : 'OK',
			},
# Other parameters
			'other_parameters' : {
				'en' : 'Other parameters',
			},
			'Accents' : {
				'en' : 'Accents',
			},
			'Anacrusis' : {
				'en' : 'Anacrusis',
			},
			'dots_and_ties' : {
				'en' : 'Dots and ties',
			},
# Other words
			'and' : {
				'en' : 'and'
			},
		}


	def get_locales(self):
		
		result = {}
		
		for key in self.Translations:
			
			# try the language of the user
			try:
				result[key] = self.Translations[key][self.Language_Code]
				
			# if the language of the user is not in the translation,
			# try english translation of this keyword
			except KeyError:
				try:
					result[key] = self.Translations[key]['en']
					
				# if the keyword is not even in english translation,
				# fall back to the keyword itself
				except KeyError:
					result[key] = key
			
		return result
