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
    parameters = {'tonic' : request.POST.get('tonic', 'C'),
                  'mode' : request.POST.get('mode', 'Major'),
                  'chords_frequency' : request.POST.get('chords_frequency', 0),
                  'intervals' : {'Second' : True},
                  'inversion' : False,
                  'display_pdf'    : False,
                  'min_pitch' : 'C',
                  'max_pitch' : "d'",
                  'rest_frequency' : 'no rests',
                  'time_signature' : '4/4',
                  'note_values' : {'1' : True, '1/2' : True, '1/4' : True},
                  'tuplets' : 'None',
                  'tuplet_same_pitch' : False,
                  'tuplets_frequency' : 'None',
                  'prolongations' : False,
                  'prolongations_frequency' : 'None',
                  'bpm' : 60,
                  'tempo' : 'andante',
                 }
    
    context.preselected = request.POST
    
    achtelbass_obj = achtelbass_web.Achtelbass(parameters, locales)
    
    context.locales  = locales
    context.generated_notes = achtelbass_obj.display()
    context.tonics = achtelbass_obj.Tonics
    context.modes  = achtelbass_obj.Modes
    context.debugging_info = achtelbass_obj.Chords_Frequency
    
    return HttpResponse(template.render(context))
