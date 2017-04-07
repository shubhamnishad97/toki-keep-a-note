from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Notes, Tag
from notes.forms import NoteForm
 
# Create your views here.
 


def index_view(request):
	notes = Notes.objects.all()
	return render(request, 'notesIndex.html', {'notes':notes})


def add_note(request):
	
	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, 'Note Added!')
			return HttpResponseRedirect(reverse('notes:index'))
	
	else:
		form = NoteForm()
		
	return render(request, 'addnote.html', {'form':form})
