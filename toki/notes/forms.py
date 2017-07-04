# /djangonote_project/djangonote/notes/forms.py
from django import forms
from notes.models import Notes, Tag
from pagedown.widgets import PagedownWidget

class NoteForm(forms.ModelForm):
	body = forms.CharField(widget=PagedownWidget)
	class Meta:
		model = Notes
		fields = ('label', 'body', 'tags')
		
class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = ('label',)