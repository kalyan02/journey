from django.forms import ModelForm
from journeyapp.models import *

class NewPostForm(ModelForm):
	class Meta:
		model = Post