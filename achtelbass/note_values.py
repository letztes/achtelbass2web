#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

class NoteValues(object):
	def __init__(self, selectable_note_values, time_signature, tuplets, tuplets_frequency):
		self.Selectable_Note_Values = selectable_note_values
		self.Time_Signature = time_signature
		self.Tuplets = tuplets
		self.Tuplets_Frequency = tuplets_frequency
		self.ABC_Note_Values = {
							 1.0	: '1',
							 1.0/2  : '2',
							 1.0/4  : '4',
							 1.0/8  : '8',
							 1.0/16 : '16',
							 1.0/32 : '32',
							 }
		self.Result = []
	
	def calculate(self):
		remaining_bar_length = self.Time_Signature # Zum Beispiel 3.0/4 = 0.75
		selectable_note_values_in_this_bar = self.Selectable_Note_Values
		abc_note_value = ''
		while remaining_bar_length > 0.0:
			selectable_note_values_in_this_bar = [selectable_note_values_in_this_bar[selectable_note_values_in_this_bar.index(item)] for item in selectable_note_values_in_this_bar if item <= remaining_bar_length]
			chosen_note_value = random.choice(selectable_note_values_in_this_bar)
			abc_note_value = self.ABC_Note_Values[chosen_note_value]
			if self.Tuplets != 0:
				if random.uniform(0, 1) < float(self.Tuplets_Frequency):
					if chosen_note_value > 1.0/32:# the tuplet note value will be smaller than the note that is broken into tuplets
						abc_note_value = int(self.ABC_Note_Values[chosen_note_value]) * 2 # half note becomes quadruplets
						tuplet = random.choice(self.Tuplets)
						self.Result.append('('+str(tuplet))
						for i in range(int(tuplet)):
							self.Result.append(str(abc_note_value))

						remaining_bar_length -= chosen_note_value
						continue
			self.Result.append(str(abc_note_value))
			remaining_bar_length -= chosen_note_value
		self.Result.append(" | ")

##############################################################################
