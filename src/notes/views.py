from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Notes, Tag
from notes.forms import NoteForm
 
# Create your views here.
 


def index_view(request):
	notes = Notes.objects.all().order_by('-timestamp')
	tags = Tag.objects.all()
	return render(request, 'notesIndex.html', {'notes':notes, 'tags':tags})



def add_note(request):


	id = request.GET.get('id', None)
	if id is not None:
		note = get_object_or_404(Notes, id=id)
	else:
		note = None
	
	if request.method == 'POST':
		if request.POST.get('control') == 'delete':
			note.delete()
			messages.add_message(request, messages.INFO, 'Note Deleted!')
			return HttpResponseRedirect(reverse('notes:index'))
		
		form = NoteForm(request.POST, instance=note)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, 'Note Added!')
			return HttpResponseRedirect(reverse('notes:index'))
	
	else:
		form = NoteForm(instance=note)
		
	return render(request, 'addNote.html', {'form':form, 'note':note})