from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

from bootstrap.forms import ExampleForm

def home(request):
    context = {}
    context["form"] = ExampleForm()
    context["user"] = request.user
    context.update(csrf(request))
    return render_to_response("bootstrap/example.html", context)

@login_required
def inside(request):
    context = {}
    context["user"] = request.user
    return render_to_response("bootstrap/inside.html", context)

