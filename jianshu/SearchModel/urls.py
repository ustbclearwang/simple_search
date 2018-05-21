from django.conf.urls import  include, url
from . import views

from django.conf import settings

urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^api/search/$',views.api_search),
]

if settings.DEBUG is False:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATICFILES_DIRS}), 
    ]
