#!/usr/bin/python
# -*- coding: utf-8 -*- 

# Author:       Artur Spengler, letztes@gmail.com
# Description:  Generates music sheet semi-randomly. Especially useful for
#               learning and practicing sight-reading.
# Licence:      GPL

import os
import random
import re
import warnings

import note_values
import pitches
import output

# Version of the program
version = '0.1'

    
class Achtelbass(object):
    """The central class of the package

       call note_values.py, pitches.py and output.py 

    """
    def __init__(self, parameters, locales):
        self.Parameters       = parameters
        self.Locales          = locales
        self.Frequency_Values = {'None' : 0,
                                 'no rests' : 0,
                                 0     : 0,
                                 '0'   : 0,
                                 '0.1' : 0.1,
                                 '0.2' : 0.2,
                                 '0.3' : 0.3,
                                 '0.4' : 0.4,
                                 '0.5' : 0.5,
                                 '0.6' : 0.6,
                                 '0.7' : 0.7,
                                 '0.8' : 0.8,
                                 '0.9' : 0.9,
                                 '1' : 1,
                                 '2' : 2,
                                 '3' : 3,
                                 '4' : 4,
                                 '5' : 5,
                                 '6' : 6,
                                 '7' : 7,
                                 '8' : 8,
                                 '9' : 9,
                                }
        self.Tuplets_Values = {'None' : 0,
                                '2' : 'x2',
                                '3' : 'x3',
                                '4' : 'x4',
                                '5' : 'x5',
                                '6' : 'x6',
                                '7' : 'x7',
                                '8' : 'x8',
                                '9' : 'x9',
                              }
        self.Fraction_Values = {'12/8' : 1.5,
                                '2/2'  : 1.0,
                                '4/4'  : 1.0,
                                '1'    : 1.0,
                                '3/4'  : 0.75,
                                '6/8'  : 0.75,
                                '1/2'  : 0.5,
                                '1/4'  : 0.25,
                                '1/8'  : 0.125,
                                '1/16' : 0.0625,
                                '1/32' : 0.03125,
                               }
        self.Diatonic_Notes          = 'C D E F G A B C'.split()
        self.Tonics                  = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F']
        self.Modes                   = ['Major', 'Minor']
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
        self.Possible_Intervals   = {v: k for k, v in self.Interval_Values.items()}
        self.Possible_Note_Values = [
                                '1',
                                '1/2',
                                '1/4',
                                '1/8',
                                '1/16',
                                '1/32',
                               ]
        self.Possible_Time_Signatures = [
                                '2/2',
                                '3/4',
                                '4/4',
                                '6/8',
                                '12/8',
                               ]

        self.Tonic                   = parameters['tonic']
        self.Mode                    = parameters['mode']
        
        if isinstance(parameters['chords_frequency'], basestring):
            self.Chords_Frequency        = float(parameters['chords_frequency'])
        elif isinstance(parameters['chords_frequency'], float):
            self.Chords_Frequency        = parameters['chords_frequency']
        else:
            self.Chords_Frequency        = 0
            
        self.Grand_Staff             = parameters['grand_staff']
        
        if isinstance(parameters['prolongations_frequency'], basestring):
            self.Prolongations_Frequency        = float(parameters['prolongations_frequency'])
        elif isinstance(parameters['prolongations_frequency'], float):
            self.Prolongations_Frequency        = parameters['prolongations_frequency']
        else:
            self.Prolongations_Frequency        = 0
        
        self.Inversion = parameters['inversion']

		# note and name are redundant here for forward compatibility reasons
        self.Note_Objects                  = [{"note":"b''", "name":"b''", "line_position": "offline",  "line_type": "ledger_line"},
                                            {"note":"a''", "name":"a''", "line_position": "online", "line_type": "ledger_line"},
                                            {"note":"g''", "name":"g''", "line_position": "offline",  "line_type": "ledger_line"},
                                            {"note":"f''", "name":"f''", "line_position": "online", "line_type": "regular_line"},
                                            {"note":"e''", "name":"e''", "line_position": "offline",  "line_type": "regular_line"},
                                            {"note":"d''", "name":"d''", "line_position": "online", "line_type": "regular_line"},
                                            {"note":"c''", "name":"c''", "line_position": "offline",  "line_type": "regular_line"},

											{"note":"b'", "name":"b'", "line_position": "offline",  "line_type": "regular_line"},
                                            {"note":"a'", "name":"a'", "line_position": "online", "line_type": "regular_line"},
                                            {"note":"g'", "name":"g'", "line_position": "offline",  "line_type": "regular_line"},
                                            {"note":"f'", "name":"f'", "line_position": "online", "line_type": "regular_line"},
                                            {"note":"e'", "name":"e'", "line_position": "offline",  "line_type": "regular_line"},
                                            {"note":"d'", "name":"d'", "line_position": "online", "line_type": "ledger_line"},
                                            {"note":"c'", "name":"c'", "line_position": "offline",  "line_type": "ledger_line"},

                                            {"note":"b", "name":"b", "line_position": "online", "line_type": "ledger_line"},
                                            {"note":"a", "name":"a", "line_position": "offline",  "line_type": "regular_line"},
                                            {"note":"g", "name":"g", "line_position": "online", "line_type": "regular_line"},
                                            {"note":"f", "name":"f", "line_position": "offline",  "line_type": "regular_line"},
                                            {"note":"e", "name":"e", "line_position": "online", "line_type": "regular_line"},
                                            {"note":"d", "name":"d", "line_position": "offline",  "line_type": "regular_line"},
                                            {"note":"c", "name":"c", "line_position": "online", "line_type": "regular_line"},

                                            {"note":"B", "name":"B", "line_position": "offline",  "line_type": "regular_line"},
                                            {"note":"A", "name":"A", "line_position": "online", "line_type": "regular_line"},
                                            {"note":"G", "name":"G", "line_position": "offline",  "line_type": "regular_line"},
                                            {"note":"F", "name":"F", "line_position": "online", "line_type": "ledger_line"},
                                            {"note":"E", "name":"E", "line_position": "offline",  "line_type": "ledger_line"},
                                            {"note":"D", "name":"D", "line_position": "online", "line_type": "ledger_line"},
                                            {"note":"C", "name":"C", "line_position": "offline",  "line_type": "ledger_line"},

                                            {"note":"B,", "name":"B,", "line_position": "online", "line_type": "ledger_line"},
                                            {"note":"A,", "name":"A,", "line_position": "offline",  "line_type": "ledger_line"},
                                            {"note":"G,", "name":"G,", "line_position": "online", "line_type": "ledger_line"},
                                            {"note":"F,", "name":"F,", "line_position": "offline",  "line_type": "ledger_line"},
                                            {"note":"E,", "name":"E,", "line_position": "online", "line_type": "ledger_line"},
                                            {"note":"D,", "name":"D,", "line_position": "offline",  "line_type": "ledger_line"},
                                            {"note":"C,", "name":"C,", "line_position": "online", "line_type": "ledger_line"}]

        self.Notes = [x["note"] for x in reversed(self.Note_Objects)]
        
        self.Min_Pitch = self.Notes[int(parameters['min_pitch'])]
        self.Max_Pitch = self.Notes[int(parameters['max_pitch'])]
        
        #if max_pitch is lower than min_pitch, swap them
        if self.Notes.index(self.Min_Pitch) > self.Notes.index(self.Max_Pitch):
            self.Min_Pitch = self.Notes[int(parameters['max_pitch'])]
            self.Max_Pitch = self.Notes[int(parameters['min_pitch'])]
        
        self.Pitch_Range = self.Notes.index(self.Max_Pitch) - self.Notes.index(self.Min_Pitch)
        
        # If pitch range is smaller than greatest interval, discard the
        # intervals that are too big
        self.Intervals = []
        for current_interval in parameters['intervals']:
            if self.Interval_Values[current_interval] <= self.Pitch_Range:
                self.Intervals.append(current_interval)
        if not self.Intervals:
            # fall back to unison
            self.Intervals = ['Unison']
        
        
        self.Clef_Left_Hand         = 'treble'
        self.Clef_Right_Hand        = 'treble'
        
        if isinstance(parameters['rest_frequency'], basestring):
            self.Rest_Frequency        = float(parameters['rest_frequency'])
        elif isinstance(parameters['rest_frequency'], float):
            self.Rest_Frequency        = parameters['rest_frequency']
        else:
            self.Rest_Frequency        = 0
        
        self.Selectable_Note_Values = [self.Fraction_Values[note_value] for note_value in parameters['note_values']]
        self.Selectable_Note_Values.sort()

        self.Time_Signature_Numerator, self.Time_Signature_Denominator = parameters['time_signature'].split('/')
        self.Time_Signature    = self.Fraction_Values[parameters['time_signature']]
        
        # if note values can not sum up to one full bar, change the
        # time signature to the greatest note value
        can_sum_up = False
        for note_value in self.Selectable_Note_Values:
            if self.Time_Signature % note_value == 0:
                can_sum_up = True
        if not can_sum_up:
            inverse_fractions   = dict([[v,k] for k,v in self.Fraction_Values.items() if '/' in k])
            self.Time_Signature = self.Selectable_Note_Values[-1]
            self.Time_Signature_Numerator, self.Time_Signature_Denominator = inverse_fractions[self.Time_Signature].split('/')
        
        self.Tuplets           = self.Tuplets_Values[parameters['tuplets']]
        self.Tuplet_Same_Pitch = parameters['tuplet_same_pitch']

        if isinstance(parameters['tuplets_frequency'], basestring):
            self.Tuplets_Frequency        = float(parameters['tuplets_frequency'])
        elif isinstance(parameters['tuplets_frequency'], float):
            self.Tuplets_Frequency        = parameters['tuplets_frequency']
        else:
            self.Tuplets_Frequency        = 0
        
        self.BPM_For_Tempo = {'grave' : 40,
                            'largo' : 44,
                            'lento' : 52,
                            'adagio' : 58,
                            'andante' : 66,
                            'moderato' : 88,
                            'allegretto' : 104,
                            'allegro' : 132,
                            'vivace' : 160,
                            'presto' : 184,
        }
        self.Tempo = parameters['tempo']
        try:
            self.BPM = parameters['bpm']
        except KeyError:
            self.BPM = self.BPM_For_Tempo[self.Tempo]

        self.Amount_Of_Bars = 8
        self.Note_String    = ''
                
        if self.Grand_Staff:
            
            range_of_tones = self.Notes.index(self.Max_Pitch) - self.Notes.index(self.Min_Pitch)
            # Left hand gets the lower 2/3
            min_pitch_left_hand = self.Min_Pitch
            max_pitch_left_hand = self.Notes[self.Notes.index(self.Max_Pitch) - int(range_of_tones/3)]
            # Right hand gets the upper 2/3
            min_pitch_right_hand = self.Notes[self.Notes.index(self.Min_Pitch) + int(range_of_tones/3)]
            max_pitch_right_hand = self.Max_Pitch
            
            note_string_left_hand  = '[V:B] '
            note_string_right_hand = '[V:T] '
            
            clef_left_hand  = 'treble'
            clef_right_hand = 'treble'
            
            self.Clef_Left_Hand = clef_left_hand
            self.Clef_Right_Hand = clef_right_hand
            
            selectable_pitches_left_hand  = self.Notes[self.Notes.index(min_pitch_left_hand):self.Notes.index(max_pitch_left_hand)+1]
            selectable_pitches_right_hand = self.Notes[self.Notes.index(min_pitch_right_hand):self.Notes.index(max_pitch_right_hand)+1]

            # Caveat, can be empty if the pitch range does not include the tonic
            # E.g. for Cmajor in F,,-G,, there is no C between F,, and G,,
            tonics_left_hand  = [note for note in selectable_pitches_left_hand  if note[0].lower() == self.Tonic[0].lower()]
            tonics_right_hand = [note for note in selectable_pitches_right_hand if note[0].lower() == self.Tonic[0].lower()]
            
            # A fifth can be only set if there are at least five notes
            # The fifth will be the starting note for the right hand
            fifth   = False
            if tonics_right_hand:
                if self.Notes.index(max_pitch_right_hand) >= self.Notes.index(tonics_right_hand[0]) + 4:
                    fifth  = self.Notes[self.Notes.index(tonics_right_hand[0]) + 4]
                elif self.Notes.index(min_pitch_right_hand) <= self.Notes.index(tonics_right_hand[0]) - 3:
                    fifth  = self.Notes[self.Notes.index(tonics_right_hand[0]) -3]
            
            previous_pitch_left_hand  = min_pitch_left_hand
            previous_pitch_right_hand = min_pitch_right_hand
            if tonics_left_hand:
                previous_pitch_left_hand  = tonics_left_hand[0]
            if tonics_right_hand:
                previous_pitch_right_hand = tonics_right_hand[0]
            
            first_bar = True
            
            # One bar after another
            for i in range(self.Amount_Of_Bars):
                note_values_left_hand = self.get_note_values(1)# one bar
                pitches_left_hand     = self.get_pitches(current_tonic  = '',
                                                min_pitch      = min_pitch_left_hand,
                                                max_pitch      = max_pitch_left_hand,
                                                note_values    = note_values_left_hand,
                                                first_note     = previous_pitch_left_hand if (first_bar) else False,
                                                previous_pitch = previous_pitch_left_hand)
                
                previous_pitch_left_hand = pitches_left_hand[-1]
                
                if i == 0 and self.Notes.index(pitches_left_hand[0]) < self.Notes.index('C'):
                    clef_left_hand = 'bass'
                    self.Clef_Left_Hand = clef_left_hand
                
                note_values_right_hand = self.get_note_values(1)
                pitches_right_hand     = self.get_pitches(current_tonic  = '',
                                                min_pitch      = min_pitch_right_hand,
                                                max_pitch      = max_pitch_right_hand,
                                                note_values    = note_values_right_hand,
                                                first_note     = fifth if (fifth and first_bar) else previous_pitch_right_hand,
                                                previous_pitch = previous_pitch_right_hand)
                
                previous_pitch_right_hand = pitches_right_hand[-1]
                
                if i == 0 and self.Notes.index(pitches_right_hand[0]) < self.Notes.index('C'):
                    clef_right_hand = 'bass'
                    self.Clef_Right_Hand = clef_right_hand
                
                bar_left_hand, clef_left_hand = self.glue_together(note_values_left_hand, pitches_left_hand, clef_left_hand)
                bar_right_hand, clef_right_hand = self.glue_together(note_values_right_hand, pitches_right_hand, clef_right_hand)
                
                note_string_left_hand  += bar_left_hand
                note_string_right_hand += bar_right_hand

                # Line break after 20 notes
                if (note_string_left_hand.count('/') > 20 or note_string_right_hand.count('/') > 20):
                    
                    # But not if it is the last iteration
                    if i < self.Amount_Of_Bars-1:
                        self.Note_String += note_string_right_hand + "\n"
                        self.Note_String += note_string_left_hand  + "\n"

                        note_string_left_hand = "[V:B "
                        note_string_right_hand = "[V:T "
                        
                        if clef_left_hand == 'bass':
                            note_string_left_hand += 'K:clef=bass] '
                        if clef_left_hand == 'treble':
                            note_string_left_hand += 'K:clef=treble] '
                        if clef_right_hand == 'bass':
                            note_string_right_hand += 'K:clef=bass] '
                        if clef_right_hand == 'treble':
                            note_string_right_hand += 'K:clef=treble] '
                        
                        note_string_left_hand += "] "
                        note_string_right_hand += "] "
                        
                first_bar = False
                    
                    
            self.Note_String += note_string_right_hand + "\n"
            self.Note_String += note_string_left_hand  + "\n"
        else:
            
            range_of_tones = self.Notes.index(self.Max_Pitch) - self.Notes.index(self.Min_Pitch)
            # Left hand gets the lower 2/3
            min_pitch_left_hand = self.Min_Pitch
            max_pitch_left_hand = self.Notes[self.Notes.index(self.Max_Pitch) - int(range_of_tones/3)]
            
            note_string_left_hand  = '[V:B] '
            
            clef_left_hand  = 'treble'
            
            self.Clef_Left_Hand = clef_left_hand
            
            selectable_pitches_left_hand  = self.Notes[self.Notes.index(min_pitch_left_hand):self.Notes.index(max_pitch_left_hand)+1]

            # Caveat, can be empty if the pitch range does not include the tonic
            # E.g. for Cmajor in F,,-G,, there is no C between F,, and G,,
            tonics_left_hand  = [note for note in selectable_pitches_left_hand  if note[0].lower() == self.Tonic[0].lower()]
            
            previous_pitch_left_hand  = min_pitch_left_hand
            if tonics_left_hand:
                previous_pitch_left_hand  = tonics_left_hand[0]
            
            first_bar = True
            
            # One bar after another
            for i in range(self.Amount_Of_Bars):
                note_values_left_hand = self.get_note_values(1)# one bar
                pitches_left_hand     = self.get_pitches(current_tonic  = '',
                                                min_pitch      = min_pitch_left_hand,
                                                max_pitch      = max_pitch_left_hand,
                                                note_values    = note_values_left_hand,
                                                first_note     = previous_pitch_left_hand if (first_bar) else False,
                                                previous_pitch = previous_pitch_left_hand)
                
                previous_pitch_left_hand = pitches_left_hand[-1]
                
                if i == 0 and self.Notes.index(pitches_left_hand[0]) < self.Notes.index('C'):
                    clef_left_hand = 'bass'
                    self.Clef_Left_Hand = clef_left_hand
                
                bar_left_hand, clef_left_hand = self.glue_together(note_values_left_hand, pitches_left_hand, clef_left_hand)
                
                note_string_left_hand  += bar_left_hand

                # Line break after 20 notes
                if (note_string_left_hand.count('/') > 20 or note_string_left_hand.count('/') > 20):
                    
                    # But not if it is the last iteration
                    if i < self.Amount_Of_Bars-1:
                        self.Note_String += note_string_left_hand  + "\n"

                        note_string_left_hand = "[V:B "
                        
                        if clef_left_hand == 'bass':
                            note_string_left_hand += 'K:clef=bass] '
                        if clef_left_hand == 'treble':
                            note_string_left_hand += 'K:clef=treble] '
                        
                        note_string_left_hand += "] "
                        
                first_bar = False
                    
                    
            self.Note_String += note_string_left_hand  + "\n"

        self.display()
        return
    
    def get_note_values(self, amount_of_bars):
        new_note_values = note_values.NoteValues(self.Selectable_Note_Values,
                                                 self.Time_Signature,
                                                 self.Tuplets,
                                                 self.Tuplets_Frequency)
        for i in range(amount_of_bars):
            new_note_values.calculate()
        
        return new_note_values.Result
    
    def get_pitches(self, current_tonic, note_values, min_pitch, max_pitch, first_note, previous_pitch):
        # current_tonic is only needed when key is changed and new tonic occurs
        
        amount = len(note_values)
        for note_value in note_values:
            if isinstance(note_value, str) and note_value.count('x'):
                tuplet_value = note_value[2:len(note_value)]
                amount += int(tuplet_value)

        if not current_tonic:
            current_tonic = self.Tonic

        new_pitches = pitches.Pitches(amount,
                                      min_pitch,
                                      max_pitch,
                                      current_tonic,
                                      self.Intervals,
                                      self.Inversion,
                                      first_note,
                                      previous_pitch)
        
        return new_pitches.easy()



    def glue_together(self, note_values, pitches, previous_clef):

        note_string = ''

        _tie_pending = False

        for i in range(len(note_values)):
            if note_values[i] == " | ":
                note_string += " | "
            else:
                    
                if random.uniform(0, 1) < self.Rest_Frequency:
                    note_string += 'z/' + note_values[i] + ' '
                else:
                
                    # If the user requested chords
                    if self.Chords_Frequency > 0:
                        # Calculate whether to show chords or not according
                        # to the propability that the user specified
                        if random.uniform(0, 1) < self.Chords_Frequency:
                            index_of_root = self.Notes.index(pitches[i])
                            
                            # Only if the root note is not too high to form a chord
                            if index_of_root + 5 <= len(self.Notes):
                                # CHANGEME septachords etc
                                # CHANGEME self.Chord_Inversion == 1 | 2 etc
                                note_string += '[' + self.Notes[index_of_root] + self.Notes[index_of_root+2] + self.Notes[index_of_root+4] + ']/' + note_values[i] + ' '
                            else:
                                note_string += pitches[i] + '/' + note_values[i] + ' '
                        else:
                            note_string += pitches[i] + '/' + note_values[i] + ' '
                    else:
                        note_string += pitches[i] + '/' + note_values[i] + ' '
                    
                
                if previous_clef == 'bass' and self.Notes.index(pitches[i]) > self.Notes.index('E'):
                    note_string += ' [K:clef=treble] '
                    previous_clef = 'treble'
                if previous_clef == 'treble' and self.Notes.index(pitches[i]) < self.Notes.index('A,'):
                    note_string += ' [K:clef=bass] '
                    previous_clef = 'bass'

        return note_string, previous_clef

    
    def display(self):
        
        new_output = output.Output(self.Tonic, self.Mode, self.Grand_Staff,
                self.Min_Pitch, self.Max_Pitch, self.Intervals,
                self.Clef_Left_Hand, self.Clef_Right_Hand, self.Note_String, self.Amount_Of_Bars,
                self.Time_Signature_Numerator,
                self.Time_Signature_Denominator, self.Locales, self.BPM)

        #print "Content-Type: text/html\n\n"
        #print ''
        #print new_output.print_out()
        return new_output.print_out()


if __name__ == '__main__':
    import getopt, sys

    def usage():
        print sys.argv[0], """is a semi random generator for sheet music."
Usage: , sys.argv[0], [OPTIONS]
None of the options are mandatory, any omitted options
are set to default values listed below.
    
Options are:
    -t, --tonic=TONIC
      default=C
    
    -m, --mode=MODE
      default=Major

    -k, --changing_key
    
    -c, --chords
    
    -l, --prolongations
    
    -q, --prolongations_frequency=FREQUENCY
      default=0.5
    
    -w, --tempo=TEMPO
      default=andante
    
    -b, --bpm=BPM
      default=60
      bpm overrides tempo if set both
    
    -i, --interval=INTERVAL1 [--interval=INTERVAL2...]
      default=Second
    
    -e, --inversion
    
    -n, --min_pitch=MIN_PITCH
      default=c4
    
    -x, --max_pitch=MAX_PITCH
      default=d5
    
    -r, --rest_frequency=REST_FREQUENCY
      default='no rests'
    
    -s, --time_signature=TIME_SIGNATURE
      default='4/4' (note the quotation marks)
    
    -v, --note_values=NOTE_VALUE1 [--note_values=NOTE_VALUE2...]
      default=1 (1 means whole notes)
    
    -u, --tuplets=TUPLETS
      default='no tuplets'
    
    -p, --tuplet_same_pitch
    
    -f, --tuplets_frequency=TUPLETS_FREQUENCY
      default='no tuplets'
    
     --help  print this message and exit
     --version print version information and exit"""
   
    # Definition of default parameters
    parameters = {'tonic' : 'C',
                  'mode' : 'Major',
                  'changing_key' : False,
                  'chords' : False,
                  'intervals' : {},
                  'inversion' : False,
                  'display_pdf'    : False,
                  'min_pitch' : 'C,',
                  'max_pitch' : "d'",
                  'rest_frequency' : 'no rests',
                  'time_signature' : '4/4',
                  'note_values' : {},
                  'tuplets' : 'None',
                  'tuplet_same_pitch' : False,
                  'tuplets_frequency' : 'None',
                  'prolongations' : False,
                  'prolongations_frequency' : 'None',
                  'bpm' : 60,
                  'tempo' : 'andante',
                 }
    pitches_opt = [
                      "C,", "D,", "E,", "F,", "G,", "A,", "B,",
                      "C", "D", "E", "F", "G", "A", "B",
                      "c", "d", "e", "f", "g", "a", "b",
                      "c'", "d'", "e'", "f'", "g'", "a'", "b'",
                      "c''", "d''", "e''", "f''", "g''", "a''", "b''",
		]
    intervals_opt = ['Unison', 'Second', 'Third', 'Fourth',
                     'Fifth', 'Sixth', 'Seventh', 'Octave']
    tempo_opt = ['grave', 'largo', 'lento', 'adagio',
                     'andante', 'moderato', 'allegretto', 'allegro',
                     'vivace', 'presto']

    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:],
                     't:m:kcid:en:x:r:s:l:v:u:pf:b:w:',
                     ['tonic=', 'mode=', 'changing_key', 'chords', 'interval=', 'no_pdf',
                      'inversion', 'min_pitch=', 'max_pitch=', 'rest_frequency=', 
                      'time_signature=', 'prolongations_frequency=',
                      'note_values=', 'tuplets=', 'tuplet_same_pitch',
                      'tuplets_frequency=', 'bpm=', 'tempo=', 'help', 'version'])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        exit()

    for opt, arg in opts:
        if opt in ('-t', '--tonic'):
            if arg in ('C', 'G', 'D', 'A', 'E', 'B', 'F#',
                       'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F'):
                parameters['tonic'] = arg
            else:
                print arg, 'is not a valid value for tonic.'
                print 'Tonic must be one of', 'C', 'G', 'D', 'A', 'E',\
                        'B', 'F#', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F'
                exit()

    for opt, arg in opts:
        if opt in ('-w', '--tempo'):
            if arg in ():
                parameters['tempo'] = arg
            else:
                print arg, 'is not a valid value for tempo.'
                print 'Tempo must be one of', str(tempo_opt[1:-1])
                exit()

    for opt, arg in opts:
        if opt in ('-b', '--bpm'):
            arg=int(arg)
            if arg >= 20 and arg <= 200:
                parameters['bpm'] = arg
            else:
                print arg, 'is not a valid value for bpm.'
                print 'Beats per minute must be an integer between 20 and 200'
                exit()

        if opt in ('-m', '--mode'):
            if arg in ('Major', 'Minor'):
                parameters['mode'] = arg
            else:
                print arg, 'is not a valid value for mode.'
                print "mode must be one of Minor, Major"
                exit()

        if opt in ('-k', '--changing_key'):
            parameters['changing_key'] = True

        if opt in ('-c', '--chords'):
            parameters['chords'] = True
            
        if opt in ('-q', '--prolongations_frequency'):
            if float(arg) >= 0 and float(arg) <= 1:
                parameters['prolongations_frequency'] = arg
            else:
                print arg, 'is not a valid value for prolongations_frequency.'
                print 'prolongations_frequency must be an integer between 0 and 1'
                print 'For example 0.5'
                exit()
            

        if opt in ('-i', '--interval'):
            if arg in (intervals_opt):
                parameters['intervals'][arg] = True
            else:
                print arg, 'is not a valid value for interval.'
                print 'interval must be one of', str(intervals_opt[1:-1])
                exit()

        if opt in ('-e', '--inversion'):
            parameters['inversion'] = True

        if opt in ('-n', '--min_pitch'):
            if arg in (pitches_opt):
                parameters['min_pitch'] = arg
            else:
                print arg, 'is not a valid value for min_pitch.'
                print 'min_pitch must be one of', str(pitches_opt)[1:-1]
                exit()

        if opt in ('-x', '--max_pitch'):
            if arg in (pitches_opt):
                parameters['max_pitch'] = arg
            else:
                print arg, 'is not a valid value for max_pitch.'
                print 'max_pitch must be one of', str(pitches_opt)[1:-1]
                exit()

        if opt in ('-r', '--rest_frequency'):
            if arg in ('no rests', '0.1', '0.2', '0.3', '0.4', '0.5'):
                parameters['rest_frequency'] = arg
            else:
                print arg, 'is not a valid value for rest_frequency.'
                print 'rest_frequency must be one of', 'no rests',\
                      '0.1', '0.2', '0.3', '0.4', '0.5'
                exit()

        if opt in ('-s', '--time_signature'):
            if arg in ('2/2', '3/4', '4/4'):
                parameters['time_signature'] = arg
            else:
                print arg, 'is not a valid value for time_signature.'
                print 'max_pitch must be one of', 'no rests', '2/2',\
                      '3/4', '4/4'
                exit()


        if opt in ('-o', '--note_values'):
            if arg in ('1', '1/2', '1/4', '1/8', '1/16', '1/32'):
                parameters['note_values'][arg] = True
            else:
                print arg, 'is not a valid value for note_values.'
                print 'note_values must be one of',\
                        "'1',", "'1/2',", "'1/4',", "'1/8',", "'1/16',", "'1/32',"
                exit()

        if opt in ('-u', '--tuplets'):
            if arg in ('no tuplets', '2', '3', '4', '5', '6', '7'):
                parameters['tuplets'] = arg
            else:
                print arg, 'is not a valid value for tuplets.'
                print 'tuplets must be one of', "'no tuplets'",\
                        '2', '3', '4', '5', '6', '7'
                exit()

        if opt in ('-p', '--tuplet_same_pitch'):
            parameters['tuplet_same_pitch'] = True

        if opt in ('-f', '--tuplets_frequency'):
            if arg in ('no tuplets', '0.1', '0.2', '0.3', '0.4', '0.5',
                       '0.6', '0.7', '0.8', '0.9', '1'):
                parameters['tuplets_frequency'] = arg
            else:
                print arg, 'is not a valid value for tuplets_frequency.'
                print 'tuplets_frequency must be one of', 'no tuplets',\
                        '0.1', '0.2', '0.3', '0.4', '0.5', '0.6',\
                        '0.7', '0.8', '0.9', '1'
                exit()
                
        if opt == '--no_pdf':
            parameters['display_pdf'] = False

        if opt == '--help':
            usage()
            exit()

        if opt in ('--version'):
            print sys.argv[0], 'version', version
            print ""
            exit()

# These two are stored in a dict of dict, so their defaults must 
# be set here separately
    if not dict(parameters['note_values']):
        parameters['note_values']['1'] = True # set default
    if not dict(parameters['intervals']):
        parameters['intervals']['Second'] = True # set default

# If time singature and note values don't fit together
    opt_fraction_values = {'2/2' : 1.0,
                            '3/4' : 0.75,
                            '4/4' : 1.0,
                            '1' : 1.0,
                            '1/2' : 0.5,
                            '1/4' : 0.25,
                            '1/8' : 0.125,
                            '1/16' : 0.0625,
                            '1/32' : 0.03125,
                           }
# When time signature is 3/4 and the only note value is 1 or 1/2, exit
    if opt_fraction_values[parameters['time_signature']] < 1:
        if '1' in parameters['note_values']:
            print 'Cannot put whole notes into '+parameters['time_signature']+' bar.'
            exit()
        if opt_fraction_values[parameters['time_signature']] != 0.5 and \
                parameters['note_values']['1/2']:
            print 'Cannot put half notes into '+parameters['time_signature']+' bar.'
            exit()

# If the span between min_pitch and max_pitch is smaller than the greatest
# interval chosen, raise an error and exit.
    names_of_chosen_intervals = parameters['intervals'].keys()
    names_of_chosen_intervals.sort()
    greatest_interval_chosen = names_of_chosen_intervals[-1]
    steps_in_note_span_chosen = abs(pitches_opt.index(parameters['max_pitch']) - pitches_opt.index(parameters['min_pitch']))
    if steps_in_note_span_chosen < intervals_opt.index(greatest_interval_chosen):
        #print steps_in_note_span_chosen; exit()
        print 'You have chosen', greatest_interval_chosen, 'as the'
        print 'greatest interval, but the span between the minimum'
        print 'pitch', parameters['min_pitch'], 'and the maximum pitch', parameters['max_pitch'], ' is only a ', intervals_opt[steps_in_note_span_chosen]+'.'
        print 'That will not fit.'
        print 'Please choose either a smaller interval or a greater'
        print "span between minimum pitch and maximum pitch.\n"
        exit()

    from locales_en import locales
    Achtelbass(parameters, locales)

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#