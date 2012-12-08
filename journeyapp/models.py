import django
from django.db import models

# Create your models here.
class Permissions(models.Model):
	name = models.CharField(max_length=200)
	time_expired = models.IntegerField(max_length=10,null=True)
	# tags = models.ManyToManyField(Tag)

	def __unicode__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=200)
	perms = models.ManyToManyField(Permissions)

	def __unicode__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=200,null=True)
	content = models.TextField(default=None,null=True)
	tags = models.ManyToManyField(Tag)
	pub_date = models.DateField(null=True)

	def __unicode__(self):
		return self.title

# class User(models.Model):
# 	username = models.CharField(max_length=200)
# 	password = models.PasswordField