#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

#TODO 

import random

class Pitches(object):
	def __init__(self, amount, min_pitch, max_pitch, tonic, intervals, inversion, first_note, previous_pitch):
		self.Amount = amount
		self.Min_Pitch = min_pitch
		self.Max_Pitch = max_pitch
		
		# Because the accidentals will be set according to the actual tonic name,
		# we don't need the sharp or b in the tonic name here.
		self.Tonic = tonic[0] # Tonart
		self.Intervals = intervals
		
		# If the next step into the randomly selected direction would
		# exceed the tonal range, reenter the tonal range on the opposite
		# side
		self.Inversion = inversion
		
		self.Notes = [
					  "C,,,", "D,,,", "E,,,", "F,,,", "G,,,", "A,,,", "B,,,",
					  "C,,", "D,,", "E,,", "F,,", "G,,", "A,,", "B,,",
					  "C,", "D,", "E,", "F,", "G,", "A,", "B,",
					  "C", "D", "E", "F", "G", "A", "B",
					  "c", "d", "e", "f", "g", "a", "b",
					  "c'", "d'", "e'", "f'", "g'", "a'", "b'",
					  "c''", "d''", "e''", "f''", "g''", "a''", "b''"
	]

		_min_index = self.Notes.index(self.Min_Pitch)
		_max_index = self.Notes.index(self.Max_Pitch)
		
		# Plus one because the slice does not include the element with the _max_index
		self.Selectable_Pitches = self.Notes[_min_index:_max_index+1]
			
		# Find all the notes within selectable span that are a tonic of the key
		tonics = [note for note in self.Selectable_Pitches if note[0].lower() == self.Tonic[0].lower()]
		
		# If the currently created bar is not the first one but in the
		# middle of the score, consider the last pitch in the previous
		# bar
		if first_note:
			self.First_Note = first_note
			
		elif previous_pitch:
			self.First_Note = previous_pitch
			
		# The first found tonic in the selectable span is the first note to print
		elif tonics:
			self.First_Note = tonics[0]
			
		# If no actual tonic found, take the lowest note in the selectable span
		else:
			self.First_Note = self.Selectable_Pitches[0]
			
		# Im nachfolgenden Dictionary wäre es nicht sinnvoll, zwischen kleinen
		# großen Intervallen zu unterscheiden, weil in den verwendeten
		# Tonleitern die Intervalle an manchen Stellen vorgegebenerweise groß
		# oder klein sind. Es ergibt sich also im Einzelfall von allein und
		# braucht nicht von vornherein definiert zu werden, es reicht wenn man
		# die Intervalle generisch benennt.
		self.Interval_Values = {
								'Unison'  : 0,
								'Second'  : 1,
								'Third'   : 2,
								'Fourth'  : 3,
								'Fifth'   : 4,
								'Sixth'   : 5,
								'Seventh' : 6,
								'Octave'  : 7,
							   }
		
		self.Result = []
	
	def easy(self):
		_current_pitch = self.First_Note
		_pre_previous_pitch = ''
		self.Result.append(_current_pitch)
		for i in range(self.Amount-1):# -1 weil der erste Ton=Tonika feststeht
			direction = random.choice(['up', 'down'])
			
			# must choose only intervals that fit at least in one direction: up or down.
			# E.g. min_pitch=C, max_pitch=c, current_pitch=F, intervals=[1,2,3,4,5,6]
			# would result in a problem if interval 5 or 6 get chosen
			# Default to Unison if nothing else fits
			_eligible_intervals = [interval for interval in self.Intervals if self.Selectable_Pitches.index(_current_pitch) + self.Interval_Values[interval] <= len(self.Selectable_Pitches) - 1 or self.Selectable_Pitches.index(_current_pitch) - self.Interval_Values[interval] >= 0] or [u'Unison']
			
			_current_interval = random.choice(_eligible_intervals)
			_step = self.Interval_Values[_current_interval]
			if self.Inversion == True:
				if (direction == 'up' and self.Selectable_Pitches.index(_current_pitch) + _step >= self.Selectable_Pitches.index(self.Selectable_Pitches[-1])) or (direction == 'down' and self.Selectable_Pitches.index(_current_pitch) - _step < 0):
					_step = _step - 7

			if direction == 'up' and self.Selectable_Pitches.index(_current_pitch) + _step <= self.Selectable_Pitches.index(self.Selectable_Pitches[-1]) and _pre_previous_pitch != self.Selectable_Pitches[self.Selectable_Pitches.index(_current_pitch)+_step]:
				_current_pitch = self.Selectable_Pitches[self.Selectable_Pitches.index(_current_pitch)+_step]
			else:
				direction = 'down'
				
			if direction == 'down' and _pre_previous_pitch != self.Selectable_Pitches[self.Selectable_Pitches.index(_current_pitch)-_step]:
				if self.Selectable_Pitches.index(_current_pitch) - _step >= 0:
					_current_pitch = self.Selectable_Pitches[self.Selectable_Pitches.index(_current_pitch)-_step]
				else:
					_current_pitch = self.Selectable_Pitches[self.Selectable_Pitches.index(_current_pitch)+_step]
			_pre_previous_pitch = _current_pitch
			self.Result.append(_current_pitch)
		return self.Result
