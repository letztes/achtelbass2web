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
				'es' : 'Inicio',
			},
			'Configuration' : {
				'en' : 'Configuration',
				'de' : 'Einstellungen',
				'es' : 'Configuración',
			},
			'Imprint' : {
				'en' : 'Imprint',
				'de' : 'Impressum',
				'es' : 'Impressum',
			},
			'About' : {
				'en' : 'About',
				'de' : 'Über achtelbass',
				'es' : 'Acerca de achtelbass',
			},
# Tooltips
			'tooltip_tonic' : {
				'en' : 'The tonic in combination with the mode yields the key of the sheet music.',
				'de' : 'Die Tonika ergibt zusammen mit dem Tongeschlecht die Tonart. Z.B. C-Dur oder A-moll. Daraus ergibt sich die Anzahl der Vorzeichen.',
				'es' : 'La tónica y el modo forman la tonalidad.',
			},
			'tooltip_intervals' : {
				'en' : 'The distance between pitches in the given key that may appear in the sheet music. When more than one interval is selected, all of them have the same probability in the random generator. There is no guarantee that an interval will occur at least one time per sheet.',
				'de' : 'Welcher Notenabstand in der zufällig generierten Musik vorkommen soll. Wenn mehrere Intervalle ausgewählt sind, sind deren Wahrscheinlichkeiten gleich groß. Es gibt allerdings keine Garantie, dass jedes Intervall mindestens ein Mal vorkommen wird.',
				'es' : 'Cuales intervales quiere a constituir las notas. No hay garantía que cada interval selecto va a aparecer en las notas, porque el generador aleatorio funciona así.',
			},
			'tooltip_note_values' : {
				'en' : 'The note values that may appear in the sheet music. When more than one note value is selected, all of them have the same probability in the begin of the measure. In the end of the measure only the smaller ones may find enough space to fit in.',
				'de' : 'Welcher Notenwert in der zufällig generierten Musik vorkommen soll. Wenn mehrere Notenwerte ausgewählt sind, sind deren Wahrscheinlichkeiten am Anfang des Taktes gleich groß. Gegen Ende des Taktes kann es passieren, dass nur noch die kleineren Notenwerte hineinpassen.',
				'es' : 'Cuales figuras quiere a constituir las notas. No hay garantía que cada figura selecta va a aparecer en las notas, porque el generador aleatorio funciona así.',
			},
			'tooltip_range' : {
				'en' : 'The lowest and the highest possible notes from which the random generator will create the sheet music.',
				'de' : 'Die niedrigst mögliche und die höchst mögliche Note, aus denen die Musik per Zufallsgenerator erstellt wird.',
				'es' : 'La nota más aguda y la nota más grave cuales el generador de números aleatorios utiliza para crear la partitura.',
			},
			'tooltip_time_signature' : {
				'en' : 'The time signature. When combined with a sole incompatible note value the note value has priority. E.g. 3/4 time signature combined with a sole 1/2 note value results in a 1/2 time signature.',
				'de' : 'Die Taktart. Wenn Notenwerte ausgewählt werden, die mit der Taktart nicht übereinstimmen, z.B. ausschließlich halbe Noten in einem 3/4 Takt, wird die Taktart an die Notenwerte angepasst, in diesem Beispiel 1/2.',
				'es' : 'El compás. La combinación de una figura y un compás incompatible resulta en un compás que sea compatible con la figura. Por ejemplo 3/4 comás combinado con una sola 1/2 figura resulta en un 1/2 compás.',
			},
			'tolltip_mode' : {
				'en' : 'The mode and the tonica yield the key signature of the sheet music.',
				'de' : 'Das Tongeschlecht in Kombination mit dem Grundton bestimmt die Tonart, d.h. die Anzahl der Vorzeichen. Dur hat eine große Terz über dem Grundton, Moll eine kleine.',
				'es' : 'El modo y la tónica forman la tonalidad. El modo mayor tiene una distancia de tercera mayor entre el primer y el tercer grado. El modo minor tiene una distancia de tercera minor el mismo lugar.',
			},
			'tooltip_grand_staff' : {
				'en' : 'Two combined staffs to be played simultaniously. One for the left hand and one for the right hand.',
				'de' : 'Zwei gleichzeitig erklingende Notenzeilen. Eine für die linke Hand und eine für die rechte Hand.',
				'es' : 'Tocar dos pentagramas simultáneamente. Uno para la mano izquiera y uno para la mano derecha.',
			},
			'tooltip_chords' : {
				'en' : 'The probability of chords. Slider left means 0%, no chords. Slider right means 100%, all notes are grouped into chords.',
				'de' : 'Die Wahrscheinlichkeit, mit der Akkorde vorkommen. Regler links bedeutet 0 %, bewirkt keinerlei Akkorde. Regler rechts bedeutet 100 %, so dass ausschließlich Akkorde und keine einzelnen Noten vorkommen.',
				'es' : 'La probabilidad con cual los acordes aparecen en las notas. Regulador a la izquierda significa 0 % probabilidad, no acordes. Regulador a la derecha significa 100 % probabilidad, todas las notas son acordes.',
			},
			'tooltip_rests' : {
				'en' : 'The probability of rests. Slider left means 0%, no rests. Slider right means 100%, all rests and no notes.',
				'de' : 'Die Wahrscheinlichkeit, mit der Pausen vorkommen. Regler links bedeutet 0%, bewirkt keinerlei Pausen. Regler rechts bedeutet 100%, so dass ausschließlich Pausen und keine Noten vorkommen.',
				'es' : 'La probabilidad con cual los silencios aparecen en las notas. Regulador a la izquierda significa 0 % probabilidad, no silencios. Regulador a la derecha significa 100 % probabilidad, todas las notas son silencios.',
			},
			'tooltip_triplets' : {
				'en' : 'The probability of triplets. Slider left means 0%, no triplets. Slider right means 100%, all notes are grouped into triplets.',
				'de' : 'Die Wahrscheinlichkeit, mit der Triolen vorkommen. Regler links bedeutet 0%, bewirkt keinerlei Triolen. Regler rechts bedeutet 100%, so dass ausschließlich Triolen und keine einzelnen Noten vorkommen.',
				'es' : 'La probabilidad con cual los trecillos aparecen en las notas. Regulador a la izquierda significa 0 % trecillos, no silencios. Regulador a la derecha significa 100 % probabilidad, todas las notas son trecillos.',
			},
# Tonic
			'Tonic' : {
				'en' : 'Tonic',
				'de' : 'Grundton',
				'es' : 'Tónica',
			},
			'C' : {
				'en' : 'C',
				'de' : 'C',
				'es' : 'Do',
			},
			'G' : {
				'en' : 'G',
				'de' : 'G',
				'es' : 'Sol',
			},
			'D' : {
				'en' : 'D',
				'de' : 'D',
				'es' : 'Re',
			},
			'A' : {
				'en' : 'A',
				'de' : 'A',
				'es' : 'La',
			},
			'E' : {
				'en' : 'E',
				'de' : 'E',
				'es' : 'Mi',
			},
			'B' : {
				'en' : 'B',
				'de' : 'B',
				'es' : 'Si',
			},
			'F#' : {
				'en' : 'F♯',
				'de' : 'F♯',
				'es' : 'Fa♯',
			},
			'C#' : {
				'en' : 'C♯',
				'de' : 'C♯',
				'es' : 'Do♯',
			},
			'G#' : {
				'en' : 'G♯',
				'de' : 'G♯',
				'es' : 'Sol♯',
			},
			'D#' : {
				'en' : 'D♯',
				'de' : 'D♯',
				'es' : 'Re♯',
			},
			'A#' : {
				'en' : 'A♯',
				'de' : 'A♯',
				'es' : 'La♯',
			},
			'Cb' : {
				'en' : 'C♭',
				'de' : 'C♭',
				'es' : 'Do♭',
			},
			'Gb' : {
				'en' : 'G♭',
				'de' : 'G♭',
				'es' : 'Sol♭',
			},
			'Db' : {
				'en' : 'D♭',
				'de' : 'D♭',
				'es' : 'Re♭',
			},
			'Ab' : {
				'en' : 'A♭',
				'de' : 'A♭',
				'es' : 'La♭',
			},
			'Eb' : {
				'en' : 'E♭',
				'de' : 'E♭',
				'es' : 'Mi♭',
			},
			'Bb' : {
				'en' : 'B♭',
				'de' : 'B♭',
				'es' : 'Si♭',
			},
			'F' : {
				'en' : 'F',
				'de' : 'F',
				'es' : 'Fa♭',
			},
# Pitch letters for output.py
			'c' : {
				'en' : 'c',
				'de' : 'c',
				'es' : 'do',
			},
			'd' : {
				'en' : 'd',
				'de' : 'd',
				'es' : 're',
			},
			'e' : {
				'en' : 'e',
				'de' : 'e',
				'es' : 'mi',
			},
			'f' : {
				'en' : 'f',
				'de' : 'f',
				'es' : 'fa',
			},
			'g' : {
				'en' : 'g',
				'de' : 'g',
				'es' : 'sol',
			},
			'a' : {
				'en' : 'a',
				'de' : 'a',
				'es' : 'la',
			},
			'b' : {
				'en' : 'b',
				'de' : 'b',
				'es' : 'si',
			},
# Mode
			'Mode' : {
				'en' : 'Mode',
				'de' : 'Tongeschlecht',
				'es' : 'Modo',
			},
			'Major' : {
				'en' : 'Major',
				'de' : 'Dur',
				'es' : 'Mayor'
			},
			'Minor' : {
				'en' : 'Minor',
				'de' : 'Moll',
				'es' : 'Menor',
			},
			'Modulation' : {
				'en' : 'Modulation',
				'de' : 'Modulation',
				'es' : 'Modulación',
			},
# Pitch / Ambitus
			'Pitch' : {
				'en' : 'Range',
				'de' : 'Tonumfang',
				'es' : 'Ámbito',
			},
# Interval
			'Interval' : {
				'en' : 'Interval',
				'de' : 'Intervall',
				'es' : 'Intervalo',
			},
			'Intervals' : {
				'en' : 'Intervals',
				'de' : 'Intervalle',
				'es' : 'Intervalos',
			},
			'Unison' : {
				'en' : 'Unison',
				'de' : 'Prime',
				'es' : 'Unísono',
			},
			'Second' : {
				'en' : 'Second',
				'de' : 'Sekunde',
				'es' : 'Segunda',
			},
			'Third' : {
				'en' : 'Third',
				'de' : 'Terz',
				'es' : 'Tercera',
			},
			'Fourth' : {
				'en' : 'Fourth',
				'de' : 'Quart',
				'es' : 'Cuarta',
			},
			'Fifth' : {
				'en' : 'Fifth',
				'de' : 'Quint',
				'es' : 'Quinta',
			},
			'Sixth' : {
				'en' : 'Sixth',
				'de' : 'Sext',
				'es' : 'Sexta',
			},
			'Seventh' : {
				'en' : 'Seventh',
				'de' : 'Septime',
				'es' : 'Séptima',
			},
			'Octave' : {
				'en' : 'Octave',
				'de' : 'Oktave',
				'es' : 'Octava',
			},
			'Inversion' : {
				'en' : 'Inversion',
				'de' : 'Inversion',
				'es' : 'Inversión',
			},
# Grand Staff
			'grand_staff' : {
				'en' : 'Grand Staff',
				'de' : 'Notation für Klavier',
				'es' : 'Notación para piano',
			},
# Rest
			'Rests' : {
				'en' : 'Rests',
				'de' : 'Pausen',
				'es' : 'Silencio',
			},
# Time signature
			'time_signature' : {
				'en' : 'Time signature',
				'de' : 'Taktart',
				'es' : 'Compás',
			},
# Note value
			'note_values' : {
				'en' : 'Note values',
				'de' : 'Notenwerte',
				'es' : 'Figuras',
			},
# Tempo
			'Tempo' : {
				'en' : 'Tempo',
				'de' : 'Tempo',
				'es' : 'Tempo',
			},
# Tuplet
			'Triplets' : {
				'en' : 'Triplets',
				'de' : 'Triolen',
				'es' : 'Tresillos',
			},
			'Tuplets' : {
				'en' : 'Tuplets',
				'de' : 'Multiolen',
				'es' : 'Grupillos',
			},
			'None' : {
				'en' : 'None',
				'de' : 'Kein',
				'es' : 'Ningún',
			},
# Chords
			'Chords' : {
				'en' : 'Chords',
				'de' : 'Akkorde',
				'es' : 'Acordes',
			},
# Configuration of website
			'enable_cookies' : {
				'en' : 'Enable cookies for saving configuration for next visit of this website',
				'de' : 'Cookies zulassen, um Einstellungen zu speichern',
				'es' : 'Permitir cookies para memorizar la configuración',
			},
			'hide_controls_after_submit' : {
				'en' : 'Hide controls after each submit on home page',
				'de' : 'Auswahlwerkzeuge auf Startseite ausgeblendet lassen nach Absenden des Formulars',
				'es' : 'Ocultar los botones en la página de inicio',
			},
			'set_amount_of_bars' : {
				'en' : 'Set amount of bars',
				'de' : 'Anzahl der Takte',
				'es' : 'Cantidad de los compases',
			},
# About div on start page
			'about_div' : {
				'en' : 'Generates sheet music in a random fashion for practicing sight reading. It uses a random number generator when picking the note values, pitches or chunks of notes so that new notes are generated in each call, thus preventing learning them by memory. Practice online for free.',
				'de' : 'Erstellt Musiknoten zufallsgenerierte Musiknoten. Notenwerte, Tonhöhen und Notengruppen werden so gewählt, dass bei jedem Seitenaufruf neues Übungsmaterial entsteht. Dadurch wird Auswendiglernen verhindert und Lesen gelernt. Kostenlos Online.',
				'es' : 'Crea notas aleatorias. Figuras, alturas y grupos de notas estan tomandos así que cada vez se forman nuevos ejercicios. Por eso uno mejora leer las notas sin memorizar los ejercicios. Gratuito online.',
			},
# About page
			'achtelbass_is_helpful' : {
				'en' : 'Achtelbass is meant to help you practice sight reading at your individual level.',
				'de' : 'Mit Achtelbass können Sie das Lesen von Noten auf Ihrem individuellen Niveau üben.',
				'es' : 'Con Achtelbass puede ejercitar leer notas a su nivel indivudal.',
			},
			'contains_random_generator' : {
				'en' : 'All notes are randomly generated and very unlikely to be seen ever again in the same combination.',
				'de' : 'Noten werden per Zufallsgenerator erstellt, so dass sie sich in derselben Kombination eher nicht mehr wiederholen werden.',
				'es' : 'Las notas estan creadas por un generador aleatorio así que no se repitan en la misma combinación.',
			},
			'free_2_play' : {
				'en' : 'Achtelbass is free of charge and does not bother you with advertisement.',
				'de' : 'Achtelbass ist kostenlos und belästigt Sie auch nicht mit Werbung.',
				'es' : 'Achtelbass es gratuido y no molesta a usted con publicidades.',
			},
			'please_contact_me' : {
				'en' : 'If you miss a feature or find a bug please contact me at',
				'de' : 'Wenn Ihnen ein Fehler auffällt oder Sie eine Funktionalität vermissen, kontaktieren Sie mich unter',
				'es' : 'Si le da cuenta de un error o si echa de menos a una funcionalidad, por favor, contacte me con', 
			},
			'please_report_issues' : {
				'en' : 'or open an issue at',
				'de' : 'oder öffnen Sie einen Vorgang unter',
				'es' : 'o cree un incidente en',
			},
# General stuff
			'hide_controls' : {
				'en' : 'Hide controls',
				'de' : 'Knöpfe verbergen',
				'es' : 'Ocultar botones',
			},
			'show_controls' : {
				'en' : 'Show controls',
				'de' : 'Knöpfe einblenden',
				'es' : 'Mostrar botones',
			},
			'generate_new' : {
				'en' : 'Generate new',
				'de' : 'Neu erstellen',
				'es' : 'Crear nuevo',
			},
			'download_midi' : {
				'en' : 'Download midi',
				'de' : 'Midi herunterladen',
				'es' : 'Descargar Midi',
			},
			'Warning' : {
				'en' : 'Warning',
				'de' : 'Warnung',
				'es' : 'Alerta',
			},
			'OK' : {
				'en' : 'OK',
				'de' : 'OK',
				'es' : 'OK',
			},
# Other parameters
			'Accents' : {
				'en' : 'Accents',
				'de' : 'Akzente',
				'es' : 'Acentuación',
			},
			'dots_and_ties' : {
				'en' : 'Dots and ties',
				'de' : 'Punkte und Bögen',
				'es' : 'Ligadura',
			},
# Other words
			'and' : {
				'en' : 'and',
				'de' : 'und',
				'es' : 'y',
			},
			'in' : { # Second and Third in C - c
				'en' : 'in',
				'de' : 'in',
				'es' : 'en',
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
		missing_translations = {'en':[], 'de':[], 'es':[]}
		
		for key in self.Translations:
			#print(key)
			for language in missing_translations:
				if language not in self.Translations[key]:
					#print(language+' '+key)
					missing_translations[language].append(key)
					
		return missing_translations
				
