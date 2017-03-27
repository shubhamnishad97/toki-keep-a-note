from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Notes
 
# Create your views here.
 
def notes(request):
    notes = Notes.objects
    template = loader.get_template('notes.html')
    context = {'notes': notes}
    return render(request, 'notes.html', context)
    #return render_to_response("note.html", notes)