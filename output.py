#!/usr/bin/python
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
        self.Notes = ["C,,", "D,,", "E,,", "F,,", "G,,", "A,,", "B,,",
                      "C,", "D,", "E,", "F,", "G,", "A,", "B,",
                      "C", "D", "E", "F", "G", "A", "B",
                      "c", "d", "e", "f", "g", "a", "b",
                      "c'", "d'", "e'", "f'", "g'", "a'", "b'"]
        
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

