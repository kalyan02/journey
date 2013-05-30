from django import forms
from django.forms import models, ModelForm, HiddenInput
from journeyapp.models import *

class TagsInput(forms.TextInput):
	def render(self,*args,**kwargs):
		kwargs['attrs'].update({
			'type':'hidden',
			})
		# args = ( args[0], ','.join(map( str,args[1]) ) )
		return super(TagsInput,self).render(*args,**kwargs)

	# on submit
	# def value_from_datadict(self,*args,**kwargs):
	def value_from_datadict(self,data,files,name):
		tags_str = data['tags']
		tags_list = tags_str.split(',')
		tags_all = []
		for each in tags_list:
			try:
				id = int(each)
				tags_all.append(id)
			except:
				if len(each) > 1:
					new_tag = Tag.objects.create(name=each)
					tags_all.append( new_tag.pk )

		return tags_all
	# def value_from_datadict(self,data,files,name):
	# 	return [1,2]

	pass

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		# exclude = ('tags',)
		widgets = {
			#'tags' : forms.TextField()
			'tags': TagsInput #Textarea(attrs={'cols': 80, 'rows': 20})
		}



class EditTagFormlet(forms.ModelForm):
	class Meta:
		model = Tag
		widgets = {
			'name' : forms.TextInput(attrs={'class':'textEdit'} ),
		}

