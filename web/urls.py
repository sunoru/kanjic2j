from django.conf.urls import patterns, url

from kanji import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)
