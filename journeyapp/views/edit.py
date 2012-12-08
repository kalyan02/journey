from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from journeyapp.forms import edit
from django.db import connection
from journeyapp.models import *
from datetime import datetime

def newpost(request):
	post_created = False
	if request.POST:
		form = edit.NewPostForm(data=request.POST)
		if form.is_valid():
			thepost = form.save()
			post_created = True
	else:		
		form = edit.NewPostForm()

	form.initial['pub_date'] = datetime.now()
	form.initial['tags'] = ('2')

	return render( request, 'edit/new.html', { 'form' : form, 'post_created':post_created } )

def editpost(request, id):
	no_form = False
	try:
		post = Post.objects.get(pk=id)
		if request.POST:
			form = edit.NewPostForm(data=request.POST, instance=post)
			if form.is_valid():
				post = form.save()
		else:
			form = edit.NewPostForm(instance=post)

	except:
		form = "Requested item does not exist!!"
		no_form = True


	return render( request, 'edit/new.html', { 'form' : form, 'post_created':False, 'no_form':no_form } )

def viewpost(request):
	if request.GET and request.GET.has_key('type_id'):
		type_id = int( request.GET['type_id'] )

		allposts = Post.objects.filter(tags__perms__pk__in=[ 1, type_id ])
		view_type = Permissions.objects.filter(pk__in=[1,type_id])
		view_type = ", ".join([ view.name for view in view_type ])
	else:
		allposts = Post.objects.all()
		view_type = None
		view_type = Permissions.objects.filter(pk=1)

	params = {
		'view_type' : view_type,
		'queries' : connection.queries,
		'allposts' : allposts
	}
	return render( request, 'edit/view.html', params )














