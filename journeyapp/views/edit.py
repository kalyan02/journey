from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from journeyapp.forms import edit
from django.db import connection
from journeyapp.models import *
from datetime import datetime
import json
from django.utils.safestring import mark_safe

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
	# form.initial['tags'] = ('2',)

	all_tags = [ { 'id' : tag.pk, 'text' : tag.name } for tag in Tag.objects.all() ]
	print "ALL TAGS", all_tags
	return render( request, 'edit/new.html', { 
		'form' : form, 
		'post_created':post_created, 
		'tags' : dir(form),
		'all_tags' : mark_safe(json.dumps(all_tags)),
		'queries' : connection.queries
	})

def editpost(request, id):
	no_form = False
	try:
		post = Post.objects.get(pk=id)
		if request.POST:
			form = edit.NewPostForm(data=request.POST, instance=post)
			if form.is_valid():
				post = form.save()
				form = edit.NewPostForm(instance=post)
		else:
			form = edit.NewPostForm(instance=post)

	except Exception, e:
		form = "Requested item does not exist!! or " + e.message
		no_form = True


	all_tags = [ { 'id' : tag.pk, 'text' : tag.name } for tag in Tag.objects.all() ]
	print all_tags
	return render( request, 'edit/new.html', {
		'form' : form,
		'post_created':False,
		'no_form':no_form,
		'all_tags' : mark_safe(json.dumps(all_tags)),
		'queries' : connection.queries
		})

def viewpost(request):
	if request.GET and request.GET.has_key('type_id'):
		type_id = int( request.GET['type_id'] )
		post_objs = Post.objects.filter(tags__perms__pk__in=[ type_id ])
		view_type = Permissions.objects.filter(pk__in=[type_id])
	else:
		post_objs = Post.objects.all()
		view_type = Permissions.objects.all()

	view_type = ", ".join([ view.name for view in view_type ])
	allposts = []
	tagPermCache = {}
	for eachPost in post_objs:
		allperms = set()
		alltags = eachPost.tags.all()
		for eachTag in alltags:
			if not tagPermCache.has_key( eachTag.id ):
				tagPermCache[ eachTag.id ] = eachTag.perms.all()

			allperms.update( tagPermCache.get( eachTag.id, [] ) )

		print allperms
		allposts.append({
				'post' : eachPost,
				'tags' : alltags,
				'perms' : allperms
			})
		# allposts = post_objs
		#view_type = Permissions.objects.filter(pk=1)

	params = {
		'view_type' : view_type,
		'queries' : connection.queries,
		'allposts' : allposts
	}
	return render( request, 'edit/view.html', params )

def edit_tags(request):
	all_tags_forms = []
	

	allOK = True
	for eachTag in Tag.objects.all():
		kwargs = {
			'instance' : eachTag, 
			'prefix' : 'tag_'+str(eachTag.id)
		}
		if request.POST:
			kwargs.update( {'data':request.POST } )

		tagFormlet = edit.EditTagFormlet( **kwargs )

		if request.POST:
			allOK = allOK and tagFormlet.is_valid()
			if not allOK:
				print 'SHIT', eachTag

		all_tags_forms.append( tagFormlet )

	if request.POST:
		if allOK:
			print 'ALL is well'
			for eachTagForm in all_tags_forms:
				eachTagForm.save()
		else:
			print 'ALL IS NOT OK'



	params = {
		'all_tags' : all_tags_forms,
		'queries' : connection.queries
	}
	return render( request, 'edit/tags.html', params )







