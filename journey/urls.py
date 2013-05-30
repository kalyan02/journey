from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'journeyapp.views.home.default', name='home'),
    url(r'^new/$', 'journeyapp.views.edit.newpost', name='new_post'),
    url(r'^edit/([\d]+)$', 'journeyapp.views.edit.editpost', name='edit_post'),
    url(r'^view/$', 'journeyapp.views.edit.viewpost', name='all_posts'),
    url(r'^tags/$', 'journeyapp.views.edit.edit_tags', name='edit_tags'),
    url(r'^perms/$', 'journeyapp.views.edit.edit_tags', name='edit_perms')

    # url(r'^journey/', include('journey.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
