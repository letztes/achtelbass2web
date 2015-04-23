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
        self.Parameters = parameters
        self.Locales = locales
        self.Frequency_Values = {'None' : 0,
                                 'no rests' : 0,
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
        self.Fraction_Values = {'2/2' : 1.0,
                                '3/4' : 0.75,
                                '4/4' : 1.0,
                                '1' : 1.0,
                                '1/2' : 0.5,
                                '1/4' : 0.25,
                                '1/8' : 0.125,
                                '1/16' : 0.0625,
                                '1/32' : 0.03125,
                               }
        self.Diatonic_Notes = 'C D E F G A B C'.split()
        self.Tonics = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F']
        self.Modes  = ['Major', 'Minor']

        self.Tonic = parameters['tonic']
        self.Mode = parameters['mode']
        #self.Key = parameters['tonic'] + '-' + parameters['mode']
        self.Intervals = parameters['intervals'].keys()
        self.Chords_Frequency = parameters['chords_frequency']
        self.Prolongations_Frequency = parameters['prolongations_frequency']
        self.Inversion = parameters['inversion']
        self.Notes = ["C,,", "D,,", "E,,", "F,,", "G,,", "A,,", "B,,",
                      "C,", "D,", "E,", "F,", "G,", "A,", "B,",
                      "C", "D", "E", "F", "G", "A", "B",
                      "c", "d", "e", "f", "g", "a", "b",
                      "c'", "d'", "e'", "f'", "g'", "a'", "b'"]
        self.Note_Letters = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
        self.Min_Pitch = parameters['min_pitch']
        self.Max_Pitch = parameters['max_pitch']
#if max_pitch is lower than min_pitch, swap them
        if self.Notes.index(self.Min_Pitch) > self.Notes.index(self.Max_Pitch):
            self.Min_Pitch = parameters['max_pitch']
            self.Max_Pitch = parameters['min_pitch']
        
        self.Rest_Frequency = self.Frequency_Values[parameters['rest_frequency']]
        self.Selectable_Note_Values = [self.Fraction_Values[note_value] for note_value in parameters['note_values'].keys()]
        self.Selectable_Note_Values.sort()

        self.Time_Signature_Numerator = parameters['time_signature'][0]
        self.Time_Signature_Denominator = parameters['time_signature'][2]
        self.Time_Signature = self.Fraction_Values[parameters['time_signature']]
        self.Tuplets = self.Tuplets_Values[parameters['tuplets']]
        self.Tuplet_Same_Pitch = parameters['tuplet_same_pitch']
        self.Tuplets_Frequency = parameters['tuplets_frequency']
        self.Display_PDF = parameters['display_pdf']
        
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

        self.Amount_Of_Bars = 40 
        self.Note_Values = self.get_note_values()
        self.Pitches = self.get_pitches()
        self.Note_String = self.glue_together()
        self.display()
    
    
    def get_note_values(self):
        new_note_values = note_values.NoteValues(self.Selectable_Note_Values,
                                                 self.Time_Signature,
                                                 self.Tuplets,
                                                 self.Tuplets_Frequency)
        for i in range(self.Amount_Of_Bars):
            new_note_values.calculate()
        
        return new_note_values.Result
    
    def get_pitches(self, current_tonic=''):
# current_tonic is only needed when key is changed and new tonic occurs
        amount = len(self.Note_Values)
        for note_value in self.Note_Values:
            if isinstance(note_value, str) and note_value.count('x'):
                tuplet_value = note_value[2:len(note_value)]
                amount += int(tuplet_value)

        if not current_tonic:
            current_tonic = self.Tonic

        new_pitches = pitches.Pitches(amount, self.Min_Pitch,
                                      self.Max_Pitch, current_tonic,
                                      self.Intervals, self.Inversion)
        
        return new_pitches.easy()



    def glue_together(self):

        note_string = ''
        
        #~ previous_pitch = self.Pitches[0]
        #~ previous_clef = 'c'
        #~ _tie_pending = False
        #~ if self.Notes.index(previous_pitch) < self.Notes.index('c4'):
            #~ previous_clef = 'b'
        
        # Line break after at least 20 notes
        note_counter = 0

        for i in range(len(self.Note_Values)):
            note_counter += 1
            if self.Note_Values[i] == " | ":
                note_string += " | "
                if note_counter > 20:
                    note_string += "\n"
                    note_counter = 0
            else:
                
                # If the user requested chords
                if int(self.Chords_Frequency) > 0:
                    
                    # Calculate whether to show chords or not according
                    # to the propability that the user specified
                    if random.randint(0,100) < int(self.Chords_Frequency):
                        index_of_root = self.Notes.index(self.Pitches[i])
                        
                        # Only if the root note is not too high to form a chord
                        if index_of_root + 4 <= len(self.Notes):
                            # CHANGEME septachords etc
                            # CHANGEME self.Chord_Inversion == 1 | 2 etc
                            note_string += '[' + self.Notes[index_of_root] + self.Notes[index_of_root+2] + self.Notes[index_of_root+4] + ']/' + self.Note_Values[i] + ' '
                        else:
                            note_string += self.Pitches[i] + '/' + self.Note_Values[i] + ' '
                    else:
                        note_string += self.Pitches[i] + '/' + self.Note_Values[i] + ' '
                else:
                    note_string += self.Pitches[i] + '/' + self.Note_Values[i] + ' '

        return note_string
    
    def display(self):
        
        new_output = output.Output(self.Tonic, self.Mode,
                self.Min_Pitch, self.Max_Pitch, self.Intervals,
                self.Pitches, self.Note_String, self.Amount_Of_Bars,
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
    pitches_opt = ["C,,", "D,,", "E,,", "F,,", "G,,", "A,,", "B,,",
                      "C,", "D,", "E,", "F,", "G,", "A,", "B,",
                      "C", "D", "E", "F", "G", "A", "B",
                      "c", "d", "e", "f", "g", "a", "b",
                      "c'", "d'", "e'", "f'", "g'", "a'", "b'"]
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
