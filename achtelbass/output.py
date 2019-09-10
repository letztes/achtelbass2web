#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

#TODO
#
#


import re

class Output(object):
	def __init__(self, tonic, mode, grand_staff, min_pitch, max_pitch, intervals, clef_left_hand, clef_right_hand, note_string, amount_of_bars, time_signature_numerator, time_signature_denominator, locales, bpm):
		self.Locales = locales
		self.Tonic = tonic
		self.Mode = mode
		self.Min_Pitch = min_pitch
		self.Max_Pitch = max_pitch
		self.Intervals = intervals
		self.Note_String  = note_string
		self.Time_Signature_Numerator = time_signature_numerator
		self.Time_Signature_Denominator = time_signature_denominator
		self.Grand_Staff = grand_staff
		self.BPM = bpm
		self.mode_abbreviation = {'Minor':'min',
								  'Major':'maj',
								 }
		self.Notes = [
			"C,,", "D,,", "E,,", "F,,", "G,,", "A,,", "B,,",
					  "C,", "D,", "E,", "F,", "G,", "A,", "B,",
					  "C", "D", "E", "F", "G", "A", "B",
					  "c", "d", "e", "f", "g", "a", "b",
					  "c'", "d'", "e'", "f'", "g'", "a'", "b'"
					  "c''", "d''", "e''", "f''", "g''", "a''", "b''"
		]
		# mode: tonic : notes with accidentals if any
		self.Title_Accidentals = {
			"Major" : {
				"C" : {},
				"G" : {"f" : "♯"},
				"D" : {
					"f" : "♯",
					"c" : "♯"
				},
				"A" : {
					"f" : "♯",
					"c" : "♯",
					"g" : "♯"
				},
				"E" : {
					"f" : "♯",
					"c" : "♯",
					"g" : "♯",
					"d" : "♯"
				},
				"B" : {
					"f" : "♯",
					"c" : "♯",
					"g" : "♯",
					"d" : "♯",
					"a" : "♯"
				},
				"F#" : {
					"f" : "♯",
					"c" : "♯",
					"g" : "♯",
					"d" : "♯",
					"a" : "♯",
					"e" : "♯"
				},
				"C#" : {
					"f" : "♯",
					"c" : "♯",
					"g" : "♯",
					"d" : "♯",
					"a" : "♯",
					"e" : "♯",
					"b" : "♯"
				},
				"Cb" : {
					"b" : "♭",
					"e" : "♭",
					"a" : "♭",
					"d" : "♭",
					"g" : "♭",
					"c" : "♭",
					"f" : "♭"
				},
				"Gb" : {
					"b" : "♭",
					"e" : "♭",
					"a" : "♭",
					"d" : "♭",
					"g" : "♭",
					"c" : "♭"
				},
				"Db" : {
					"b" : "♭",
					"e" : "♭",
					"a" : "♭",
					"d" : "♭",
					"g" : "♭"
				},
				"Ab" : {
					"b" : "♭",
					"e" : "♭",
					"a" : "♭",
					"d" : "♭"
				},
				"Eb" : {
					"b" : "♭",
					"e" : "♭",
					"a" : "♭"
				},
				"Bb" : {
					"b" : "♭",
					"e" : "♭",
				},
				"F" : {"b" : "♭"}
			},
			"Minor" : {
				"A" : {},
				"E" : {"f" : "♯"},
				"B" : {
					"f" : "♯",
					"c" : "♯"
				},
				"F#" : {
					"f" : "♯",
					"c" : "♯",
					"g" : "♯"
				},
				"C#" : {
					"f" : "♯",
					"c" : "♯",
					"g" : "♯",
					"d" : "♯"
				},
				"G#" : {
					"f" : "♯",
					"c" : "♯",
					"g" : "♯",
					"d" : "♯",
					"a" : "♯"
				},
				"D#" : {
					"f" : "♯",
					"c" : "♯",
					"g" : "♯",
					"d" : "♯",
					"a" : "♯",
					"e" : "♯"
				},
				"A#" : {
					"f" : "♯",
					"c" : "♯",
					"g" : "♯",
					"d" : "♯",
					"a" : "♯",
					"e" : "♯",
					"b" : "♯"
				},
				"Ab" : {
					"b" : "♭",
					"e" : "♭",
					"a" : "♭",
					"d" : "♭",
					"g" : "♭",
					"c" : "♭",
					"f" : "♭"
				},
				"Eb" : {
					"b" : "♭",
					"e" : "♭",
					"a" : "♭",
					"d" : "♭",
					"g" : "♭",
					"c" : "♭"
				},
				"Bb" : {
					"b" : "♭",
					"e" : "♭",
					"a" : "♭",
					"d" : "♭",
					"g" : "♭"
				},
				"F" : {
					"b" : "♭",
					"e" : "♭",
					"a" : "♭",
					"d" : "♭"
				},
				"C" : {
					"b" : "♭",
					"e" : "♭",
					"a" : "♭"
				},
				"G" : {
					"b" : "♭",
					"e" : "♭",
				},
				"D" : {"b" : "♭"}
			},
		}
		
		## Hier faengt die Definition der Praeambelelemente an.
		
		# Anzahl logischer Schlaege im ersten Auftakt. Dezimalbrueche moeglich.
		self.Auftaktschlaege = 0
		
		## Namen der Instrumente, von unten nach oben.
		# Wird vor das jeweilige Notensystem geschrieben.
		# Kann leergelassen werden.
		#self.Instrument_Name = 'Blockfloete'
		self.Instrument_Name = ''

		self.Clef_Left_Hand = clef_left_hand
		self.Clef_Right_Hand = clef_right_hand
		
		## Titel des Stuecks.
		#Wird zusammengestellt aus den Intervallen und dem Notenumfang.
		intervals_string = ''
		for interval in self.Intervals:
			intervals_string += self.Locales[interval] + ', '
		intervals_string = re.sub(', $', ' '+locales['in']+' ', intervals_string)
		intervals_string = re.sub(r'(.+),(.+?)$', r'\g<1> '+locales['and']+' \g<2>', intervals_string)
			
		min_pitch_letter = re.findall(r"[A-G]", self.Min_Pitch, re.IGNORECASE)[0] # for finding accidentals
		min_pitch_corrected = re.sub(min_pitch_letter, locales[min_pitch_letter], self.Min_Pitch) # Do for C in spanish
		# only if there exists an accidental for that letter, add it
		if min_pitch_letter.lower() in self.Title_Accidentals[self.Mode][self.Tonic]:
			# self.Title_Accidentals = mode: tonic : notes with accidentals if any
			min_pitch_corrected = min_pitch_corrected + self.Title_Accidentals[self.Mode][self.Tonic][min_pitch_letter.lower()]
		
		max_pitch_letter = re.findall(r"[A-G]", self.Max_Pitch, re.IGNORECASE)[0] # for finding accidentals
		max_pitch_corrected = re.sub(max_pitch_letter, locales[max_pitch_letter], self.Max_Pitch) # Do for C in spanish
		if max_pitch_letter.lower() in self.Title_Accidentals[self.Mode][self.Tonic]:
			max_pitch_corrected = max_pitch_corrected + self.Title_Accidentals[self.Mode][self.Tonic][max_pitch_letter.lower()]
		
		
		
		self.Title = intervals_string + min_pitch_corrected + ' - ' + max_pitch_corrected # usw.
	
	def print_out(self):
	   
		output_string = ''
		# Zunaechst die Praeambel
		praeambel = "X:1\n" # Some sort of header marking
		praeambel += "T:" + self.Title + "\n"
		praeambel += "M:" + self.Time_Signature_Numerator + "/" + self.Time_Signature_Denominator + "\n" # 4/4 or so
		praeambel += "K:" + self.Tonic + self.mode_abbreviation[self.Mode] + "\n" # The Key
		praeambel += "L:" + '4/4' + "\n" # The reference note length
		if self.BPM:
			praeambel += "Q:1/4=" + str(self.BPM) + "\n"
		
		if self.Grand_Staff:
			praeambel += "V:T clef="+ self.Clef_Right_Hand +"\n"
			praeambel += "V:B clef="+ self.Clef_Left_Hand +"\n"
		else:
			praeambel += "K:" + 'clef='+self.Clef_Left_Hand + "\n" # The Key
		
		
		output_string += praeambel
				
		# An dieser Stelle werden die eigentlichen Noten gesetzt.
		output_string += self.Note_String + "\n"
		
		return output_string

