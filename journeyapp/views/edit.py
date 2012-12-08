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


	# print dir(form.name)
	# form['title'] = "FOo"

	form.initial['pub_date'] = datetime.now()

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
		allposts = Post.objects.filter(tags__perms__pk=int(request.GET['type_id']))
	else:
		allposts = Post.objects.all()

	all_tags = Tag.objects.all()
	public_tag = all_tags.filter(name='Public')
	# first_tag = Tag.objects.get(pk=1)
	# thef_tag = Tag.objects.get(pk=1)

	# queries = ""
	# for each in connection.queries:
	# 	queries += str(each)

	params = {
		'alist' : public_tag,
		'queries' : connection.queries,
		'allposts' : allposts
	}
	return render( request, 'edit/view.html', params )