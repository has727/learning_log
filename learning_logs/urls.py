#! /usr/bin/env python3

from django.conf.urls import url

from learning_logs.views import index, topics, topic, new_topic, new_entry, edit_entry

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^topics/$', topics, name='topics'),
	url(r'^topic/(?P<topic_id>\d+)/$', topic, name='topic'),
	url(r'^new_topic/$', new_topic, name='new_topic'),
	url(r'^new_entry/(?P<topic_id>\d+)/$', new_entry, name='new_entry'),
	url(r'^edit_entry/(?P<entry_id>\d+)/$', edit_entry, name='edit_entry'),
]
