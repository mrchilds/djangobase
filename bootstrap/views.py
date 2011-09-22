from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.utils import simplejson

from bootstrap.forms import ExampleForm, AjaxAutoComplete, PopoverForm
from bootstrap.models import StarWarsCharacter

def home(request):
    context = {}
    context.update(csrf(request))
    context["user"] = request.user
    context["hero_title"] = "Welcome to django base"
    return render_to_response("bootstrap/home.html", context)


def ajax_form(request):
    context = {}
    context["form"] = ExampleForm()
    context["user"] = request.user
    context["hero_title"] = "Ajax Form"
    context.update(csrf(request))
    return render_to_response("bootstrap/example.html", context)


def ajax_example(request):
    context = {}
    if request.POST:
        form = ExampleForm(request.POST)
        if form.is_valid():
            #Do Something, e.g. save, send an email
            template = "bootstrap/example_form_success.html"
            success = True
        else:
            template = "bootstrap/example_form.html"
            context["form"] = form
            success = False
    else:
        template = "bootstrap/example_form.html"
        context["form"] = ExampleForm()
        success = False
    html = render_to_string(template, context)
    response = simplejson.dumps({"success": success, "html": html})
    return HttpResponse(response,
                        content_type=\
                            "application/javascript; charset=utf-8")    


def modal_dialog(request):
    context = {}
    context["user"] = request.user
    context["hero_title"] = "Modal Dialog"
    context.update(csrf(request))
    return render_to_response("bootstrap/modal/modal_dialog.html", context)


def text_modal_dialog(request):
    if request.POST.get('id', False):
        # String provided for ease of demonstration
        # Replace with model lookup, e.g. 
        # wording = User.objects.get(id=request.POST.get('id', False))
        wording = "ABC"
    else:
        wording = False
    template = "bootstrap/modal/modal_dialog_text.html"
    html = render_to_string(template, {"wording": wording})
    response = simplejson.dumps({"html": html})
    return HttpResponse(response,
                        content_type=\
                            "application/javascript; charset=utf-8")
                                                    

def ajax_autocomplete(request):
    context = {}
    context["user"] = request.user
    context["hero_title"] = "Ajax Autocomplete"
    context["form"] = AjaxAutoComplete()
    context.update(csrf(request))
    return render_to_response("bootstrap/autocomplete/autocomplete.html", context)


def ajax_autocomplete_lookup(request):
    results = []
    if request.GET.has_key("term"):
        value = request.GET[u'term']
        characters = StarWarsCharacter.objects.filter(name__icontains=value)
        for character in characters:
            character_dict = {}
            character_dict["id"] = character.id
            character_dict["label"] = character.name
            results.append(character_dict)   
    response = simplejson.dumps(results)
    return HttpResponse(response,
                        content_type=\
                            "application/javascript; charset=utf-8")


def ajax_autocomplete_get_selected_item(request):
    character_id = request.POST.get("character_id", False)
    if character_id:
        try:
            character = StarWarsCharacter.objects.get(id=character_id)
        except StarWarsCharacter.DoesNotExist:
            character = None
    else:
        character = None
    template = "bootstrap/autocomplete/select_result.html"
    html = render_to_string(template, {"character": character})
    response = simplejson.dumps({"html": html})
    return HttpResponse(response,
                        content_type=\
                            "application/javascript; charset=utf-8")
                            
                            
def popover(request):
    context = {}
    context["user"] = request.user
    context["hero_title"] = "Popovers"
    context["form"] = PopoverForm()
    context.update(csrf(request))
    return render_to_response("bootstrap/popover/popover.html", context)


def geolocation(request):
    context = {}
    context["user"] = request.user
    context["hero_title"] = "Geolocation"
    context.update(csrf(request))
    return render_to_response("bootstrap/geolocation/geolocation.html", context)
    
    
@login_required
def inside(request):
    context = {}
    context["user"] = request.user
    return render_to_response("bootstrap/inside.html", context)

