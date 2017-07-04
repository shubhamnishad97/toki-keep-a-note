from django.conf.urls import include, url
from django.contrib import admin
from notes.views import index_view, add_note, add_tag


urlpatterns = [
    url(r'^$', index_view, name='index'),
	url(r'^addnote/', add_note, name='addnote'),
	url(r'^addtag/', add_tag, name='addtag'),
]