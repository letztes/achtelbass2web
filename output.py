#!/usr/bin/python
# -*- coding: utf-8 -*- 

#TODO
#
#


import re

class Output(object):
    def __init__(self, tonic, mode, min_pitch, max_pitch, intervals, pitches, note_string, amount_of_bars, time_signature_numerator, time_signature_denominator, locales, bpm):
        self.Locales = locales
        self.Tonic = tonic
        self.Mode = mode
        self.Min_Pitch = min_pitch
        self.Max_Pitch = max_pitch
        self.Intervals = intervals
        self.Note_String = note_string
        self.Time_Signature_Numerator = time_signature_numerator
        self.Time_Signature_Denominator = time_signature_denominator
        self.BPM = bpm
        self.mode_abbreviation = {'Minor':'min',
                                  'Major':'maj',
                                 }
        
        ## Hier faengt die Definition der Praeambelelemente an.
        ## Zwoelf Zahlen stehen als erstes in der Praeambel, durch whitespace
        ## getrennt.
        ## Die ersten acht beprint_out musikalische Daten.
        
        # Anzahl der Notensysteme (relativ zu der Anzahl der Instrumente)
        self.Amount_Of_Note_Systems = 1
        
        self.Amount_Of_Instruments = 1	# Anzahl der Instrumente
        
        # Anzahl logischer Schlaege im ersten Auftakt. Dezimalbrueche moeglich.
        self.Auftaktschlaege = 0
        
        # Anzahl der Notensysteme, d.h. gedruckter Partiturzeilen
        self.Amount_Of_Systems = amount_of_bars / 4
        self.Size_Of_System = 16 # Groesse eines Notensystems in pt
        
        ## Namen der Instrumente, von unten nach oben.
        # Wird vor das jeweilige Notensystem geschrieben.
        # Kann leergelassen werden.
        #self.Instrument_Name = 'Blockfloete'
        self.Instrument_Name = ''
        
        ## Clef, von unten nach oben.
        # b heisst Bassschluessel, t heisst Violinschluessel.
        # Wird in get_clef() berechnet.
        self.Clef = self.get_clef(pitches[0])
        self.Clef_Vormals = self.Clef

        ## Das Directory, in das die Tex-Datei geschrieben werden soll.
        self.Directory = './'
        
        ## Titel des Stuecks.
        #Wird zusammengestellt aus den Intervalsn und dem Notenumfang.
        intervals_string = ''
        for interval in self.Intervals:
            intervals_string += self.Locales[interval] + ', '
        intervals_string = re.sub(r', $', r' in ', intervals_string)
        intervals_string = re.sub(r'(.+),(.+?)$', r'\g<1> '+locales['and']+' \g<2>', intervals_string)
        self.Title = intervals_string + self.Min_Pitch + ' - ' + self.Max_Pitch # usw.
    
    def print_out(self):
       
        output_string = ''
        # Zunaechst die Praeambel
        praeambel = "X:1\n" # Some sort of header marking
        praeambel += "T:" + self.Title + "\n"
        praeambel += "M:" + self.Time_Signature_Numerator + "/" + self.Time_Signature_Denominator + "\n" # 4/4 or so
        praeambel += "K:" + self.Tonic + self.mode_abbreviation[self.Mode] + "\n" # The Key
        praeambel += "L:" + self.Time_Signature_Numerator + '' + "/" + self.Time_Signature_Denominator + "\n" # 4/4 or so # The reference note length
        
        
        output_string += praeambel
                
        # An dieser Stelle werden die eigentlichen Noten gesetzt.
        output_string += self.Note_String + "\n"#CHANGEME
        #output_string += "|dedB dedB|c2ec B2dB|" + "\n"
        
        return output_string
        
    
    def get_clef(self, notenhoehe):
        if re.search(r"[4567]$", notenhoehe):
            return 't'
        if re.search(r"[123]$", notenhoehe):
            return 'b'

