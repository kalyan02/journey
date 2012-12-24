from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def default(request):

	#sql = "SELECT social_auth_usersocialauth.id, social_auth_usersocialauth.user_id, social_auth_usersocialauth.provider, social_auth_usersocialauth.uid, social_auth_usersocialauth.extra_data, auth_user.id, auth_user.username, auth_user.first_name, auth_user.last_name, auth_user.email, auth_user.password, auth_user.is_staff, auth_user.is_active, auth_user.is_superuser, auth_user.last_login, auth_user.date_joined FROM social_auth_usersocialauth INNER JOIN auth_user ON (social_auth_usersocialauth.user_id = auth_user.id) WHERE social_auth_usersocialauth.user_id = 1"

	pre = None

	return render( request, 'index.html', {'pre':pre} )