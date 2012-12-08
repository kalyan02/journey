from django.dispatch import dispatcher
from django.db.models.signals import post_syncdb
from journeyapp	import models as app

def journey_backpack( **kwargs ):
	print "Setting up default data"
	public_tag = app.Tag.objects.create( name='Public' )
	private_tag = app.Tag.objects.create( name='Private' )

	public_perm = app.Permissions.objects.create( name='Public' )
	private_perm = app.Permissions.objects.create( name='Private' )

	public_tag.perms.add( public_perm )
	private_tag.perms.add( private_perm )

	public_tag.save()
	private_tag.save()

	pass

post_syncdb.connect( journey_backpack, sender=app )