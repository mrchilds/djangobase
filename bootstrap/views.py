from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.utils import simplejson

from bootstrap.forms import ExampleForm


def home(request):
    context = {}
    context.update(csrf(request))
    context["user"] = request.user
    return render_to_response("bootstrap/home.html", context)


def ajax_form(request):
    context = {}
    context["form"] = ExampleForm()
    context["user"] = request.user
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


@login_required
def inside(request):
    context = {}
    context["user"] = request.user
    return render_to_response("bootstrap/inside.html", context)

