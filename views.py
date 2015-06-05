# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

import achtelbass_web
from locales_en import locales
locales_inverse = dict([[v,k] for k,v in locales.items()]) #CHANGEME braucht man das?

def index(request):
    template = loader.get_template('generate_notes/index.html')
    context = RequestContext(request, {})
    context.generated_notes = 'abc'
    parameters = {'tonic'                   : request.POST.get('tonic', 'C'),
                  'mode'                    : request.POST.get('mode', 'Major'),
                  'grand_staff'             : request.POST.get('grand_staff', False),
                  'chords_frequency'        : request.POST.get('chords_frequency', 0),
                  'intervals'               : request.POST.getlist('intervals', ['Second']),
                  'inversion'               : False,
                  'display_pdf'             : False,
                  'min_pitch'               : request.POST.get('min_pitch', 'E,,'),
                  'max_pitch'               : request.POST.get('max_pitch', "d"),
                  'rest_frequency'          : request.POST.get('rest_frequency', 0),
                  'time_signature'          : '4/4',
                  #'note_values'             : {'1' : True, '1/2' : True, '1/4' : True},
                  #'note_values'             : ['1', '1/2', '1/4'],
                  'note_values'             : request.POST.getlist('note_values', ['1', '1/2', '1/4']),
                  'tuplets'                 : 'None',
                  'tuplet_same_pitch'       : False,
                  'tuplets_frequency'       : 'None',
                  'prolongations'           : False,
                  'prolongations_frequency' : 'None',
                  'bpm'                     : 60,
                  'tempo'                   : 'andante',
                 }
    
    
    achtelbass_obj = achtelbass_web.Achtelbass(parameters, locales)
    
    context.__dict__.update(achtelbass_obj.__dict__)
    
    context.preselected = request.POST.copy()
    
    # The multiselect is one zero byte separated string, we want a list
    context.preselected.intervals_list    = request.POST.getlist('intervals')
    context.preselected.note_values_list  = request.POST.getlist('note_values')
    
    context.generated_notes = achtelbass_obj.display()
#    context.debugging_info  = achtelbass_obj.Chords_Frequency
    
    return HttpResponse(template.render(context))
