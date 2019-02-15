#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Locales(object):
	def __init__(self, language_code):
		
		self.Language_Code = language_code
		
		self.Translations = {
# Menu
			'Home' : {
				'en' : 'Home',
				'de' : 'Startseite',
			},
			'Configuration' : {
				'en' : 'Configuration',
				'de' : 'Einstellungen',
			},
			'Imprint' : {
				'en' : 'Imprint',
				'de' : 'Impressum',
			},
			'About' : {
				'en' : 'About',
				'de' : 'Über achtelbass',
			},
# Tonic
			'Tonic' : {
				'en' : 'Tonic',
				'de' : 'Grundton',
			},
			'C' : {
				'en' : 'C',
				'de' : 'C',
			},
			'G' : {
				'en' : 'G',
				'de' : 'G',
			},
			'D' : {
				'en' : 'D',
				'de' : 'D',
			},
			'A' : {
				'en' : 'A',
				'de' : 'A',
			},
			'E' : {
				'en' : 'E',
				'de' : 'E',
			},
			'B' : {
				'en' : 'B',
				'de' : 'B',
			},
			'F#' : {
				'en' : 'F♯',
				'de' : 'F♯',
			},
			'C#' : {
				'en' : 'C♯',
				'de' : 'C♯',
			},
			'G#' : {
				'en' : 'G♯',
				'de' : 'G♯',
			},
			'D#' : {
				'en' : 'D♯',
				'de' : 'D♯',
			},
			'A#' : {
				'en' : 'A♯',
				'de' : 'A♯',
			},
			'Gb' : {
				'en' : 'G♭',
				'de' : 'G♭',
			},
			'Db' : {
				'en' : 'D♭',
				'de' : 'D♭',
			},
			'Ab' : {
				'en' : 'A♭',
				'de' : 'A♭',
			},
			'Eb' : {
				'en' : 'E♭',
				'de' : 'E♭',
			},
			'Bb' : {
				'en' : 'B♭',
				'de' : 'B♭',
			},
			'F' : {
				'en' : 'F',
				'de' : 'F',
			},
# Mode
			'Mode' : {
				'en' : 'Mode',
				'de' : 'Tongeschlecht',
			},
			'Major' : {
				'en' : 'Major',
				'de' : 'Dur',
			},
			'Minor' : {
				'en' : 'Minor',
				'de' : 'Moll',
			},
			'Modulation' : {
				'en' : 'Modulation',
				'de' : 'Modulation',
			},
# Pitch / Ambitus
			'Pitch' : {
				'en' : 'Range',
				'de' : 'Tonumfang',
			},
# Interval
			'Interval' : {
				'en' : 'Interval',
				'de' : 'Intervall',
			},
			'Intervals' : {
				'en' : 'Intervals',
				'de' : 'Intervalle',
			},
			'Unison' : {
				'en' : 'Unison',
				'de' : 'Prime',
			},
			'Second' : {
				'en' : 'Second',
				'de' : 'Sekunde',
			},
			'Third' : {
				'en' : 'Third',
				'de' : 'Terz',
			},
			'Fourth' : {
				'en' : 'Fourth',
				'de' : 'Quart',
			},
			'Fifth' : {
				'en' : 'Fifth',
				'de' : 'Quint',
			},
			'Sixth' : {
				'en' : 'Sixth',
				'de' : 'Sext',
			},
			'Seventh' : {
				'en' : 'Seventh',
				'de' : 'Septime',
			},
			'Octave' : {
				'en' : 'Octave',
				'de' : 'Oktave',
			},
			'Inversion' : {
				'en' : 'Inversion',
				'de' : 'Inversion',
			},
# Grand Staff
			'grand_staff' : {
				'en' : 'Grand Staff',
				'de' : 'Klaviersystem',
			},
# Rest
			'Rests' : {
				'en' : 'Rests',
				'de' : 'Pausen',
			},
# Time signature
			'time_signature' : {
				'en' : 'Time signature',
				'de' : 'Taktart',
			},
# Note value
			'note_values' : {
				'en' : 'Note values',
				'de' : 'Notenwerte',
			},
# Tempo
			'Tempo' : {
				'en' : 'Tempo',
				'de' : 'Tempo',
			},
# Tuplet
			'Triplets' : {
				'en' : 'Triplets',
				'de' : 'Triolen',
			},
			'Tuplets' : {
				'en' : 'Tuplets',
				'de' : 'Multiolen',
			},
			'None' : {
				'en' : 'None',
				'de' : 'Kein',
			},
# Chords
			'Chords' : {
				'en' : 'Chords',
				'de' : 'Akkorde',
			},
# Configuration of website
			'enable_cookies' : {
				'en' : 'Enable cookies for saving configuration for next visit of this website',
				'de' : 'Cookies zulassen, um Einstellungen zu speichern',
			},
			'hide_controls_after_submit' : {
				'en' : 'Hide controls after each submit on home page',
				'de' : 'Auswahlwerkzeuge auf Startseite ausgeblendet lassen nach Absenden des Formulars',
			},
			'set_amount_of_bars' : {
				'en' : 'Set amount of bars',
				'de' : 'Anzahl der Takte',
			},
# About page
			'achtelbass_is_helpful' : {
				'en' : 'Achtelbass is meant to help you practice sight reading at your individual level.',
				'de' : 'Mit Achtelbass können Sie das Lesen von Noten auf Ihrem individuellen Niveau üben.',
			},
			'contains_random_generator' : {
				'en' : 'All notes are randomly generated and very unlikely to be seen ever again in the same combination.',
				'de' : 'Noten werden per Zufallsgenerator erstellt, so dass sie sich in derselben Kombination eher nicht mehr wiederholen werden.',
			},
			'no_memorization_effect' : {
				'en' : 'This way you will not memorize the notes of the exercise as it happens often with traditional literature.',
				'de' : 'Dadurch vermeiden Sie das Auswendiglernen von Notenmaterial, was leider mit traditioneller Übungsliteratur häufig vorkommt.',
			},
			'achtelbass_is_versatile' : {
				'en' : 'You can increase the difficulty level gradually by adding options evenly or concentrate on certain options like triplets, chords, exotic time signatures or whatever you want to master.',
				'de' : 'Sie können den Schwierigkeitsgrad gemäß Ihrem persönlichen Lernfortschritt erhöhen oder sich auf bestimmte Aspekte wie Triolen, Akkorde oder exotische Taktarten konzentrieren.',
			},
			'achtelbass_is_versatile_really' : {
				'en' : 'Prepare for exams, target your personal weak spots or just begin to learn sight reading.',
				'de' : 'Bereiten Sie sich auf Prüfungen vor, gehen Sie Ihre Schwachstellen an oder beginnen Sie einfach nur damit, endlich Notenlesen zu lernen.',
			},
			'free_2_play' : {
				'en' : 'Achtelbass is free of charge and does not bother you with advertisement.',
				'de' : 'Achtelbass ist kostenlos und belästigt Sie auch nicht mit Werbung.',
			},
			'please_contact_me' : {
				'en' : 'If you miss a feature or find a bug please contact me at',
				'de' : 'Wenn Ihnen ein Fehler auffällt oder Sie eine Funktionalität vermissen, kontaktieren Sie mich unter',
			},
			'please_report_issues' : {
				'en' : 'or open an issue at',
				'de' : 'oder öffnen Sie einen Vorgang unter',
			},
			'please_fork_the_repo' : {
				'en' : 'If you are into python then you might fork the project and fix the issue by yourself.',
				'de' : 'Wenn Sie gerne in Python programmieren, können Sie zum Projekt direkt beitragen.',
			},
			'request_for_donation' : {
				'en' : 'If you do not code but like the website and want to contribute you can make a donation.',
				'de' : 'Wenn Ihnen das Programmieren nicht liegt, Sie die Webseite aber gerne unterstützen möchten, können Sie einen kleinen Betrag spenden.',
			},
# General stuff
			'hide_controls' : {
				'en' : 'Hide controls',
				'de' : 'Knöpfe verbergen',
			},
			'show_controls' : {
				'en' : 'Show controls',
				'de' : 'Knöpfe einblenden',
			},
			'generate_new' : {
				'en' : 'Generate new',
				'de' : 'Neu erstellen',
			},
			'download_midi' : {
				'en' : 'Download midi',
				'de' : 'Midi herunterladen',
			},
			'Warning' : {
				'en' : 'Warning',
				'de' : 'Warnung',
			},
			'OK' : {
				'en' : 'OK',
			},
# Other parameters
			'Accents' : {
				'en' : 'Accents',
				'de' : 'Akzente',
			},
			'dots_and_ties' : {
				'en' : 'Dots and ties',
				'de' : 'Punkte und Bögen',
			},
# Other words
			'and' : {
				'en' : 'and',
				'de' : 'und',
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
	
	def get_missing_translations(self):
		
		# This is the place to define which languages to check
		# Add new language by adding 'xy':[] to the list of keys here
		missing_translations = {'en':[], 'de':[],}
		
		for key in self.Translations:
			#print(key)
			for language in missing_translations:
				if language not in self.Translations[key]:
					#print(language+' '+key)
					missing_translations[language].append(key)
					
		return missing_translations
				
