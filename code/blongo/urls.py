from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'blongo.blogapp.views.index'),
    url(r'^update/', 'blongo.blogapp.views.update'),
    url(r'^delete/', 'blongo.blogapp.views.delete'),
    url(r'^user/', 'blongo.blogapp.views.user_details'),                   
)
